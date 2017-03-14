from django.contrib import admin
from moddle.models import UserProfile, Bike, Booking
#from moddle.models import Booking

def user_username(self):
    return self.user.username

def first_name(self):
    return self.user.first_name
    
def last_name(self):
    return self.user.last_name

class UserProfileAdmin(admin.ModelAdmin):
    list_display = (user_username, first_name, last_name)

class BikeAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')

# class BookingAdmin(admin.ModelAdmin):
#     list_display = ('owner', 'borrower')

# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Bike, BikeAdmin)
admin.site.register(Booking)