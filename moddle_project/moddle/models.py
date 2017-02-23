from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class User(models.Model):
	username = models.CharField(max_length=128, unique=True)
	full_name = models.CharField(max_length=128)
	email = models.EmailField(max_length=128)
	phone_number = models.CharField(max_length=16, blank=True)
	gender_male = models.BooleanField()
	post_code = models.CharField(max_length=7)

	def __str__(self):
		return self.username
	# for python 2.7
	def __unicode__(self):
		return self.username

class Bike(models.Model):
	name = models.CharField(max_length=128)
	owner = models.ForeignKey(User)
	boys_bike = models.BooleanField()
	adults_bike = models.BooleanField()
	description = models.CharField(max_length=512, unique=True)
	bike_picture = models.ImageField()
	bike_picture = models.ImageField(upload_to='profile_images', blank=True)

	def __str__(self):
		return self.name
	# for python 2.7
	def __unicode__(self):
		return self.name

class Booking(models.Model):