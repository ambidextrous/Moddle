from django import forms
from django.contrib.auth.models import User
from moddle.models import Bike, UserProfile, Booking

# Added to attempt to resolve incorrect password registration problem		
from django.utils.translation import ugettext, ugettext_lazy as _


class UserForm(forms.ModelForm):
    # This masks the password as it is typed, instead of the default
    # behaviour of displaying the password in plain text
    password = forms.CharField(widget=forms.PasswordInput())

    # Nested Meta class - describes additional poperties.
    # Each Meta class must supply a model field.
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
        ## could also have fields to exclude here

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone_number', 'gender_male', 'post_code', 'profile_picture')

class BikeForm(forms.ModelForm):
	name = forms.CharField(max_length=128, help_text="Please enter the name/title of your bike.")
	boys_bike = forms.BooleanField(help_text="Tick if this is a men's bike, leave unticked for women's:", required=False)
	adults_bike = forms.BooleanField(help_text="Tick if this is an adult's bike:", required=False)
	description = forms.CharField(max_length=500, help_text="Please give a short description of your bike:", required=True)

	class Meta:
		# Provide an association between the ModelForm and a model
		model = Bike
		fields = ('name', 'boys_bike', 'adults_bike', 'description', 'bike_picture')

class BookingForm(forms.ModelForm):
    start_date = forms.DateField(help_text="Starting date (suggest form: Y-m-d)")
    finish_date = forms.DateField(help_text="Ending date (suggest form: Y-m-d)")

    class Meta:
        model = Booking
        fields = ('start_date', 'finish_date')
        



