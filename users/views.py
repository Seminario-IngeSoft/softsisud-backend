# User Views

#Django
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Exception
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User
from users.models import Profile

#form
from users.forms import ProfileForm, SignupForm

# Create your views here.
def login_view(request):
    """ Login view"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Prueba en local
        # print(username, ':', password)
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('posts:feed') # urls.py
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})

    # Si el usuario ya está autenticado
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('posts:feed')

    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('users:login')

# Signup por medio de vistas
def signup_view(request):
    """ Signup view """
    #Debugger
    # import pdb;pdb.set_trace()
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['passwd']
        passwd_confirmation = request.POST['passwd_confirmation']

        if passwd != passwd_confirmation:
            return render(request, 'users/signup_view.html', {'error': 'Password confirmation does not match'})

        try:
            user = User.objects.create_user(username=username, password=passwd)
        except IntegrityError:
            return render(request, 'users/signup_view.html', {'error': 'Username is already in user'})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.save()
        return redirect('users:login')

    return render(request, 'users/signup_view.html')

# Signup por medio de form
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = SignupForm()

    return render(
        request=request,
        template_name='users/signup.html',
        context={'form': form}
    )

def update_profile(request):
    """Update a users profile view """
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()

            print(form.cleaned_data)

            url = reverse('users:detail', kwargs={'username': request.user.username})
            return redirect(url)
    else:
        form = ProfileForm()

    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile':profile,
            'user':request.user,
            'form':form
        }
    )
