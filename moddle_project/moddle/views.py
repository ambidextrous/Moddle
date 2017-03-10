from django.shortcuts import render
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from moddle.models import User, UserProfile, Bike
from moddle.forms import UserForm, UserProfileForm
# Imported to send lat-long info
from django.http import JsonResponse

def get_user_object(request):
    if request.user.is_authenticated():
        current_user = request.user
        print current_user.username
        return current_user
    else:
        print "Not logged in"
        return None

def index(request):
    context_dict = {'': ''}
    return render(request, 'moddle/index.html', context=context_dict)

def user_profile(request, username):
    # Create a context dictionary which we can pass to the template rendering engine
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.

        user = User.objects.get(username=username)
        userprofile = UserProfile.objects.get(user=user)
        context_dict['userprofile'] = userprofile

        # Retrieve all of the associated bikes.
        # Note that filter() will return a list of bike objects or an empty list
        users_bikes = Bike.objects.filter(owner=userprofile)
        context_dict['bikes'] = users_bikes

    except UserProfile.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything -
        # the template will display the "no category" message for us.
        print "User does not exist"
        context_dict['bikes'] = None
        context_dict['userprofile'] = None

    return render(request, 'moddle/user_profile.html', context=context_dict)


def user_login(request):
    # If the request is a HTTP POST, try to pull out the relevant information
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        # We use request.POST.get('<variable>') as opposed
        # to request.POST['<variable>'], because the
        # request.POST.get('<variable>') returns None if the
        # value does not exist, while request.POST['<variable>']
        # will raise a KeyError exception.
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
                return HttpResponseRedirect(reverse('index'))
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print("Invalid login details for user: {0}, {1}".format(username, password))
            return HttpResponse(
                "Invalid login details supplied. The supplied password in combination with the username '" + username + "' were incorrect.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'moddle/login.html', {})

def register(request):
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
            user.save

            # Now sort out the UserProfile instance
            # Since we need to set the user attribute ourselves,
            # we set commit=False. This delays saving the model
            # until we're ready to avoid integrity problems
            profile = profile_form.save(commit=False)
            profile.user = user

            # Now we save the UserProfile model instance
            profile.save()

            # Update our variable to indicate that the template
            # registration was successful
            registered = True
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

def search(request):
    context_dict = {'': ''}
    return render(request, 'moddle/search.html', context=context_dict)

@login_required
def upload_bike(request, username):
    if request.user.is_authenticated and str(request.user.username) == username:
        print request.user.username

    # check page 117 in tango with django to use this for uploading a picture.
    # Did the user provide a profile picture?
    # If so, we need to get it from the input form and
    # put it in the UserProfile model
    #if 'picture' in request.FILES:
    #    profile.picture = request.FILES['picture']

    context_dict = {'': ''}
    return render(request, 'moddle/upload_bike.html', context=context_dict)

def bike_profile(request):
    context_dict = {'': ''}
    return render(request, 'moddle/bike_profile.html', context=context_dict)

@login_required
def request_bike(request):
    context_dict = {'': ''}
    return render(request, 'moddle/request_bike.html', context=context_dict)

@login_required
def view_bookings(request):
    context_dict = {'': ''}
    return render(request, 'moddle/view_bookings.html', context=context_dict)

def faq(request):
    context_dict = {'': ''}
    return render(request, 'moddle/faq.html', context=context_dict)

def contact_us(request):
    context_dict = {'': ''}
    return render(request, 'moddle/contact_us.html', context=context_dict)

def about(request):
    context_dict = {'': ''}
    return render(request, 'moddle/about.html', context=context_dict)

def storelatlong(request):
    print "Get here!"
    context_dict = {'': ''}
    lat = float(request.GET.get('lat', ''))
    lng = float(request.GET.get('lng', ''))
    print "lat = "+lat
    print "lng = "+lng
    resp_data = {'lat': lat, 'lng': lng}
    return JsonResponse(resp_data)
