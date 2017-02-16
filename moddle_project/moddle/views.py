from django.shortcuts import render

def index(request):
    context_dict = {'': ''}
    return render(request, 'moddle/index.html', context=context_dict)

def user_profile(request):
    context_dict = {'': ''}
    return render(request, 'moddle/user_profile.html', context=context_dict)

def login(request):
    context_dict = {'': ''}
    return render(request, 'moddle/login.html', context=context_dict)

def register(request):
    context_dict = {'': ''}
    return render(request, 'moddle/register.html', context=context_dict)

def search(request):
    context_dict = {'': ''}
    return render(request, 'moddle/search.html', context=context_dict)

def upload_bike(request):
    context_dict = {'': ''}
    return render(request, 'moddle/upload_bike.html', context=context_dict)

def bike_profile(request):
    context_dict = {'': ''}
    return render(request, 'moddle/bike_profile.html', context=context_dict)

def request_bike(request):
    context_dict = {'': ''}
    return render(request, 'moddle/request_bike.html', context=context_dict)

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