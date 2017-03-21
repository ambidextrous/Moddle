from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
import datetime

import os

# Helper method to
def get_bike_image_folder(instance, filename):
    if os.name == 'nt':
        return "bikes/%s/%s" % (instance.owner.user.username, filename)
    else:
        return "bikes\%s\%s" % (instance.owner.user.username, filename)

def get_user_image_folder(instance, filename):
    if os.name == 'nt':
        return "profile_pictures/%s/%s" % (instance.user.username, filename)
    else:
        return "profile_pictures\%s\%s" % (instance.user.username, filename)
        
class UserProfile(models.Model):
    user = models.OneToOneField(User)

    # The additional attributes we wish to include
    about_me = models.CharField(max_length=512, blank=True)
    phone_number = models.CharField(max_length=16, blank=True)
    gender = models.CharField(max_length=16)
    post_code = models.CharField(max_length=7)
    longitude = models.FloatField(null=True, blank=True, default=-4.2924705147743225)
    latitude = models.FloatField(null=True, blank=True, default=55.87371280304047)
    profile_picture = models.ImageField(upload_to=get_user_image_folder, blank=True)

    def __str__(self):
        return self.user.username
    # for python 2.7
    def __unicode__(self):
        return self.user.username

class Bike(models.Model):
    name = models.CharField(max_length=128)
    owner = models.ForeignKey(UserProfile)
    category = models.CharField(max_length=20)
    bike_gender = models.CharField(max_length=16)
    bike_age = models.CharField(max_length=16)
    description = models.CharField(max_length=512, blank=True)
    bike_picture = models.ImageField(upload_to=get_bike_image_folder, blank=True)
    price_per_day = models.FloatField(null=True, blank=True, default=0.0)

    def __str__(self):
        return self.name
    # for python 2.7
    def __unicode__(self):
        return self.name

class Booking(models.Model):
    start_date = models.DateField()
    finish_date = models.DateField()
    owner = models.ForeignKey(UserProfile, related_name='owner')
    borrower = models.ForeignKey(UserProfile, related_name='borrower')
    bikeid = models.ForeignKey(Bike)
    booking_approved = models.NullBooleanField(blank=True)
    
    def __str__(self):
        return self.id

    def __unicode__(self):
        return self.borrower.__str__()
        
