from django.contrib import admin
from moddle.models import UserProfile, Bike
#from moddle.models import Booking

def user_username(self):
    return self.user.username

class UserProfileAdmin(admin.ModelAdmin):
    list_display = (user_username, 'post_code')

class BikeAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')

# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Bike, BikeAdmin)