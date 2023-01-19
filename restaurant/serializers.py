from rest_framework import serializers
from .models import Menu, Booking
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        models = Menu
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        models = Booking
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']