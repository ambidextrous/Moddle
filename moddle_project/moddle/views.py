from django.shortcuts import render
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from moddle.models import User, UserProfile, Bike, Booking
from moddle.forms import UserForm, UserProfileForm, BikeForm, BookingForm
from django.shortcuts import redirect
# Imported to send lat-long info
from django.http import JsonResponse
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
# User notifications
from django.contrib import messages

#Attempt to make a RESTful API for the map page
from rest_framework import viewsets
from moddle.serializers import UserSerializer, CoordinatesSerializer, BikeSerializer

def get_user_object(request):
    if request.user.is_authenticated():
        current_user = request.user
        print current_user.username
        return current_user
    else:
        print "Not logged in"
        return None

def index(request):
    # Request the context of the request
    # The context contains information of all available bikes

    context_dict = {}

    if request.method == 'GET' and request.META['QUERY_STRING']:
 
        try:
            bike_list = Bike.objects.all()
            query_set = []

            bike_gender = request.GET.get('bike_gender')
            if bike_gender != '0':
                query_set.append(bike_gender)
                bike_list = bike_list.filter(bike_gender=bike_gender)

            bike_age = request.GET.get('bike_age')
            if bike_age != '0':
                query_set.append(bike_age)
                bike_list = bike_list.filter(bike_age=bike_age)

            category = request.GET.get('category')
            if category != '0':
                query_set.append(category)
                bike_list = bike_list.filter(category=category)

            context_dict['bikes'] = bike_list
            if len(query_set) == 0:
                context_dict['query_set'] = None
            else:
                context_dict['query_set'] = query_set

        except Bike.DoesNotExist:
            print 'Cannot find'

    else:
        context_dict['bikes'] = Bike.objects.all()
    return render(request, 'moddle/index.html', context=context_dict)

def user_profile(request, username):
    # Create a context dictionary which we can pass to the template rendering engine
    context_dict = {}

    try:
        # Find a userprofile given the username slug
        user = User.objects.get(username=username)
        userprofile = UserProfile.objects.get(user=user)
        context_dict['userprofile'] = userprofile

        # Retrieve all of the associated bikes.
        # Note that filter() will return a list of bike objects or an empty list
        users_bikes = Bike.objects.filter(owner=userprofile)
        context_dict['bikes'] = users_bikes
        
    except UserProfile.DoesNotExist:
        print "User does not exist"
        context_dict['bikes'] = None
        context_dict['userprofile'] = None
	
    print context_dict
    return render(request, 'moddle/user_profile.html', context=context_dict)

def map(request):
    # Create a context dictionary which we can pass to the template rendering engine
    context_dict = {}

    try:
        bike_list = Bike.objects.all()
        context_dict['bike_list'] = bike_list
        
    except Bike.DoesNotExist:
        print "Bike does not exist"

    return render(request, 'moddle/map.html', context=context_dict)
    
def user_login(request):
    if request.user.is_authenticated: 
        return HttpResponseRedirect(reverse('index'))
    # If the request is a HTTP POST, try to pull out the relevant information
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                # confirmation message
                messages.success(request, 'Login successful.')
                return HttpResponseRedirect(reverse('index'))
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print("Invalid login attempt with details: {0}, {1}".format(username, password))
            messages.error(request, 'The supplied password in combination with the username "' + username + '" were incorrect.')
            return HttpResponseRedirect(reverse('login'))

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'moddle/login.html', {})

def register(request):
    if request.user.is_authenticated: 
        return HttpResponseRedirect(reverse('index'))
    # A boolean value for telling the template
    # whether the registration was successful.
    # Set to False initially. Code changes value to
    # True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database
            user = user_form.save()

            # Now we hash the password with the set_password method
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance
            # Since we need to set the user attribute ourselves,
            # we set commit=False. This delays saving the model
            # until we're ready to avoid integrity problems
            
            profile = profile_form.save(commit=False)
            profile.user = user

            try:
                profile.latitude = float(request.POST.get('userLat'))
                profile.longitude = float(request.POST.get('userLong'))
            except ValueError:
                profile.latitude = 55.87371280304047 
                profile.longitude = -4.2924705147743225

            # If user provides a bike picture?
            if 'profile_picture' in request.FILES:
                profile.profile_picture = request.FILES.get('profile_picture', None)
            
            # Now we save the UserProfile model instance
            profile.save()
            
            # confirmation message	
            messages.success(request, 'Account created successfully.')	

            # Update our variable to indicate that the template
            # registration was successful
            registered = True
            print("User detail: {0}, {1}".format(user, user.password))
        else:
            # Invalid form or forms - mistakes or something else?
            # Print problems to the terminal.
            print(user_form.errors, profile_form.errors)
    else:
        # Not a HTTP POST, so we render our form using two ModelForm instances
        # These forms will be blank, ready for user input.
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context
    return render(request,
                  'moddle/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return HttpResponseRedirect(reverse('index'))

@login_required
def upload_bike(request, username):

    owner = UserProfile.objects.get(user=request.user)
    form = BikeForm()

    if request.method == 'POST':
        form = BikeForm(request.POST)

        if form.is_valid():
            bike = form.save(commit=False)

            # Retrieve the associated information
            bike.owner = owner

            # If user provides a bike picture?
            if 'bike_picture' in request.FILES:
                bike.bike_picture = request.FILES.get('bike_picture', None)
            
            bike.price_per_day = round(float(request.POST.get('price_per_day')),2)	
            
            bike.save()
            
            # confirmation message
            messages.success(request, 'Thank you, your bike has been uploaded.')
            
            return HttpResponseRedirect(reverse('index'))
        else:
            print form.errors

    context_dict = {'form':form}

    return render(request, 'moddle/upload_bike.html', context=context_dict)

def bike_profile(request, bike_id_slug):
    # Create a context dictionary which we can pass to the template rendering engine
    # test: bike_id = 9
    context_dict = {}

    try:
        # Can we find a bike with the given bike id slug?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.

        bike = Bike.objects.get(id=bike_id_slug)

        context_dict['bike'] = bike

        userprofile = bike.owner
        context_dict['userprofile'] = userprofile		
		
    except Bike.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything -
        # the template will display the "no category" message for us.
        print "Bike does not exist"
        context_dict['bike'] = None

    return render(request, 'moddle/bike_profile.html', context=context_dict)

@login_required
def request_bike(request, bike_id_slug):

    bike = Bike.objects.get(id=bike_id_slug)
    owner = bike.owner
    borrower = UserProfile.objects.get(user=request.user)

    form = BookingForm()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        print("Booking detail: {0} {1} {2}".format(bike, owner, borrower))

        if form.is_valid():
            booking = form.save(commit=False)

            # Retreive the booking information
            booking.owner = owner
            booking.borrower = borrower
            booking.bikeid = bike
            booking.save()

            # confirmation message
            messages.success(request, 'Bike request was sent to ' + owner.user.username + ' successfully.')	
            
            return HttpResponseRedirect(reverse('index'))
        else:
            messages.error(request, 'Invalid details...')	
            print form.errors

    context_dict = {'bike': bike, 'form':form}
    return render(request, 'moddle/request_bike.html', context=context_dict)

@login_required
def view_bookings(request, username):

    user = User.objects.get(username=username)
    
    # check if the requester is authenticated and if it is their own bookings page.
    if request.user.is_authenticated and request.user == user:

        user_profile = UserProfile.objects.get(user=user)
        context_dict = {}
        
        try:
            # Return all the bookings made by the user
            bookings_made = Booking.objects.filter(borrower=user_profile)
            context_dict['bookings_made'] = bookings_made
        except Booking.DoesNotExist:
            # Don't do anything -
            # the template will display the "no booking" message for us.
            print "No booking by this user"

        try:
            # Return all the bookings made by the user
            bookings_received = Booking.objects.filter(owner=user_profile)
            context_dict['bookings_received'] = bookings_received
        except Booking.DoesNotExist:
            # Don't do anything -
            # the template will display the "no booking" message for us.
            print "No booking for this users bikes"

        return render(request, 'moddle/view_bookings.html', context=context_dict)
    
    else:
        # user has no business being here
        return HttpResponseRedirect(reverse('index'))

def faq(request):
    context_dict = {'': ''}
    return render(request, 'moddle/faq.html', context=context_dict)

def contact_us(request):
    context_dict = {'': ''}
    return render(request, 'moddle/contact_us.html', context=context_dict)

def about(request):
    context_dict = {'': ''}
    return render(request, 'moddle/about.html', context=context_dict)

@login_required
def storelatlong(request):
    context_dict = {'': ''}
    lat = float(request.GET.get('lat', ''))
    lng = float(request.GET.get('lng', ''))
    profile = request.user.userprofile
    profile.latitude = lat
    profile.longitude = lng
    profile.save()
    return HttpResponse("OK")

@login_required
def delete_bike(request, bike_id_slug):
    try:
        # Find the bike with the given bike id slug
        bike = Bike.objects.get(id=bike_id_slug)		
        if request.user.userprofile == bike.owner:
            bike.delete()
            
            # confirmation message
            messages.error(request, 'Your bike has been successfully deleted.')		
			
    except Bike.DoesNotExist:
        print "Bike does not exist"

    return HttpResponseRedirect(reverse('user_profile', args=[request.user.username]))
    
@login_required
def delete_booking(request, booking_id):
    try:
        # Find the booking with the given bike id slug
        booking = Booking.objects.get(id=booking_id)		
        if request.user.userprofile == booking.borrower:
            booking.delete()
            
            # confirmation message
            messages.error(request, 'Your booking has been successfully deleted.')		
			
    except Booking.DoesNotExist:
        print "Booking does not exist"

    return HttpResponseRedirect(reverse('view_bookings', args=[request.user.username]))

@login_required
def approve_booking(request, booking_id):
    try:
        # Find the booking with the given bike id slug
        booking = Booking.objects.get(id=booking_id)
        if request.user.userprofile == booking.owner:
            booking.booking_approved = True
            booking.save()
            # confirmation message
            messages.success(request, 'Booking successfully approved.')				
			
    except Booking.DoesNotExist:
        print "booking does not exist"

    #return redirect('view_bookings', username=request.user.username)
    return HttpResponseRedirect(reverse('view_bookings', args=[request.user.username]))

@login_required
def reject_booking(request, booking_id):
    try:
        # Find the booking with the given bike id slug
        booking = Booking.objects.get(id=booking_id)
        if request.user.userprofile == booking.owner:
            booking.booking_approved = False
            booking.save()
            
            # confirmation message
            messages.error(request, 'Booking successfully rejected.')
			
    except Booking.DoesNotExist:
        print "booking does not exist"

    return HttpResponseRedirect(reverse('view_bookings', args=[request.user.username]))

##Attempt to make a RESTful API for the map page
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class CoordinatesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows coordinates to be viewed or edited.
    """
    queryset = UserProfile.objects.all()
    serializer_class = CoordinatesSerializer
    
class BikeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer
    