from django import forms
from django.contrib.auth.models import User
from moddle.models import Bike, UserProfile

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
        fields = ('phone_number', 'gender_male', 'post_code')

<<<<<<< HEAD
# Added to attempt to resolve incorrect password registration problem		
class UserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'duplicate_username': _("A user with that username already exists."),
        'password_mismatch': _("The two password fields didn't match."),
    }
    username = forms.RegexField(label=_("Username"), max_length=30,
        regex=r'^[\w.@+-]+$',
        help_text=_("Required. 30 characters or fewer. Letters, digits and "
                      "@/./+/-/_ only."),
        error_messages={
            'invalid': _("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")})
    password1 = forms.CharField(label=_("Password"),
        widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"),
        widget=forms.PasswordInput,
        help_text=_("Enter the same password as above, for verification."))

    class Meta:
        model = User
        fields = ("username",)

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'])
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user		
		
		
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

=======
>>>>>>> af17882a65bc1e9ad51e54ddaa3381ce63c40731

class BikeForm(forms.ModelForm):
	name = forms.CharField(max_length=128, help_text="Please enter the name of bike.")
	boys_bike = forms.BooleanField()
	adults_bike = forms.BooleanField()
	description = forms.CharField(max_length=500, help_text="Make people know your bike.")

	class Meta:
		# Provide an association between the ModelForm and a model
		model = Bike
		fields = ('name', 'boys_bike', 'adults_bike', 'description')


