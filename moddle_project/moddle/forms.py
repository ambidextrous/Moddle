from django import forms
from django.contrib.auth.models import User
from moddle.models import Bike, UserProfile, Booking

# Added to attempt to resolve incorrect password registration problem        
from django.utils.translation import ugettext, ugettext_lazy as _


class UserForm(forms.ModelForm):
    # This masks the password as it is typed, instead of the default
    # behaviour of displaying the password in plain text
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    
    # Nested Meta class - describes additional poperties.
    # Each Meta class must supply a model field.
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
        ## could also have fields to exclude here

class UserProfileForm(forms.ModelForm):
    about_me = forms.CharField(widget=forms.Textarea, max_length=512, required=True)
    phone_number = forms.CharField(max_length=16)
    post_code = forms.CharField(max_length=16)
    
    genders=[('Male', 'Male'), ('Female','Female'), ('Other','Other')]
    gender = forms.ChoiceField(choices=genders)
    
    class Meta:
        model = UserProfile
        fields = ('phone_number', 'gender', 'post_code', 'profile_picture', 'about_me')

class BikeForm(forms.ModelForm):

    name = forms.CharField(max_length=128, help_text="Please enter the name/title of your bike.")
    
    bike_genders = [('Mens', 'Mens'), ('Womens','Womens'), ('Other','Other')]
    bike_gender = forms.ChoiceField(help_text="Bike gender: ", choices=bike_genders)
    bike_ages = [('Adults', 'Adults'), ('Teens','Teens'), ('Childs','Childs')]
    bike_age = forms.ChoiceField(help_text="Suitable age: ", choices=bike_ages)
    categories = [('Mountainbike', 'Mountainbike'), ('Cross Country','Cross Country'), ('Road Bike','Road Bike'), ('City Bike','City Bike'), ('Electric Bike','Electric Bike'), ('Unicycle','Unicycle'), ('Tricycle','Tricycle'), ('BMX','BMX'), ('Other','Other')]
    category = forms.ChoiceField(help_text="Type of bike: ", choices=categories)

    description = forms.CharField(widget=forms.Textarea, max_length=512, help_text="Please give a short description of your bike: ", required=True)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Bike
        fields = ('name', 'bike_gender', 'bike_age', 'category', 'description', 'bike_picture')

class BookingForm(forms.ModelForm):
    start_date = forms.DateField(help_text="Starting date (suggest form: Y-m-d)")
    finish_date = forms.DateField(help_text="Ending date (suggest form: Y-m-d)")

    class Meta:
        model = Booking
        fields = ('start_date', 'finish_date')
