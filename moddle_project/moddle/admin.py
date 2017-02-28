from django.contrib import admin
from moddle.models import User, Bike
#from moddle.models import Booking

class UserAdmin(admin.ModelAdmin):
	list_display = ('username', 'full_name', 'post_code')

class BikeAdmin(admin.ModelAdmin):
	list_display = ('name', 'owner')

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Bike, BikeAdmin)