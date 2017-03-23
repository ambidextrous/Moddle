from django.contrib.auth.models import User
from moddle.models import Bike, UserProfile
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

def user_username(self):
    return self.user.username

class CoordinatesSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = UserProfile
        fields = ('user','longitude', 'latitude')

class BikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bike
        fields = ('name', 'description')