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
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
        ## could also have fields to exclude here

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone_number', 'gender_male', 'post_code')

"""bike form
class CategoryForm(forms.ModelForm):
	name = forms.CharField(max_length=128,
		help_text="Please enter the category name.")
	view = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)
	
	# An inline class to provide additional information on the form.
	# Perhaps the most important aspect of a class inheriting from ModelForm
	# is the need to define which model we're wanting to provide a form for.
	# We take care of this through our nested Meta class. Set the model
	# attribute of the nested Meta class to the model you wish to use.
	class Meta:
		# Provide an association between the ModelForm and a model
		model = Category
		# this is a list of only the forms you want to display to the user.
		fields = ('name',)


class PageForm(forms.ModelForm):
	title = forms.CharField(max_length=128,
		help_text="Please enter the title of the page.")
	url = forms.URLField(max_length=128,
		help_text="Please enter the URL of the page.")
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

	class Meta:
		# Provide an association between the ModelForm and a model
		model = Page
		
		# What fields do we want to include in our form?
		# This way we don't need every field in the model present.
		# Some fields may allow NULL values, so we may not want to include them.
		# Here, we are hiding the foreign key.
		# we can either exclude the category field from the form,
		exclude = ('category',)
		# or specify the fields to include (i.e. not include the category field)
		#fields = ('title', 'url', 'views')
		
		def clean(self):
			cleaned_data = self.cleaned_data
			url = cleaned_data.get('url')
			
			# if url is not empty and doesn't start with 'http://',
			# then prepend 'http://'
			if url and not url.startswith('http://'):
				url = 'http://' + url
				
				return cleaned_data
"""


