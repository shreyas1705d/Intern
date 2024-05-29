from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignupForm, LoginForm
from .models import CustomUser

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('success')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def home_view(request):
    return render(request, 'home.html')

def success_view(request):
    return render(request, 'success.html')

def logout_view(request):
    logout(request)
    return redirect('home')



