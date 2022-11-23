from .models import Profile, User
from .serializers import ProfileSerializer, UsersSerializer
from rest_framework import viewsets
from django.contrib.auth import get_user_model

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class UsersViewSet(viewsets.ModelViewSet):
    user = get_user_model()
    queryset = user.objects.all()
    serializer_class = UsersSerializer