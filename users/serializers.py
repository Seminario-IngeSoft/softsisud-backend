from .models import Profile
from rest_framework import serializers
from django.contrib.auth import get_user_model
#from django.contrib.auth.models import User

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        user = get_user_model()
        model = user
        #model = User
        fields = '__all__'