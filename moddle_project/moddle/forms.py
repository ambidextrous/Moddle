from django import forms
from django.contrib.auth.models import User
from moddle.models import Bike, UserProfile

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
        fields = ('phone_number', 'gender_male', 'post_code')


class BikeForm(forms.ModelForm):
	name = forms.CharField(max_length=128, help_text="Please enter the name of bike.")
	boys_bike = forms.BooleanField()
	adults_bike = forms.BooleanField()
	description = forms.CharField(max_length=500, help_text="Make people know your bike.")

	class Meta:
		# Provide an association between the ModelForm and a model
		model = Bike
		fields = ('name', 'boys_bike', 'adults_bike', 'description')


