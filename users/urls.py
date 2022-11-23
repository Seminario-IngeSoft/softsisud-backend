"""Platzigram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
# Users urls
from users import views as users_views
from django.views.generic import TemplateView

# Django rest framework
from rest_framework import routers

# Api
from users import viewsApi

router = routers.DefaultRouter()
router.register('users_profiles', viewsApi.ProfileViewSet)
#router.register('users_list', viewsApi.UsersSerializer)

app_name = 'users'
urlpatterns = [
    # Management
    path('login',users_views.login_view, name="login" ),
    path('logout',users_views.logout_view, name="logout" ),
    path('signup/view',users_views.signup_view, name="signup_view" ),
    path('signup',users_views.signup, name="signup" ),

    #Middlewares
    path('me/profile', users_views.update_profile, name="update_profile" ),

    # API
    path('api/', include(router.urls)),
]
