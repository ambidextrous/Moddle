from django.shortcuts import render
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

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

def user_profile(request, username=None):

    context_dict = {'': ''}
    return render(request, 'moddle/user_profile.html', context=context_dict)

def login(request):
    context_dict = {'': ''}
    return render(request, 'moddle/login.html', context=context_dict)

@login_required	
def logout(request):
    return HttpResponseRedirect(reverse('index'))

def register(request):
    context_dict = {'': ''}
    return render(request, 'moddle/register.html', context=context_dict)

def search(request):
    context_dict = {'': ''}
    return render(request, 'moddle/search.html', context=context_dict)

@login_required
def upload_bike(request, username):
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