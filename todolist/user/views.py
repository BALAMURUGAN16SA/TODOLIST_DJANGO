from django.shortcuts import render, redirect
from .forms import CustomForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def base(response):
    return render(response, 'user/base.html', {})

def signup(response):
    form = CustomForm()
    if response.method == 'POST':
        form = CustomForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    return render(response, 'user/signup.html', {"form":form})

def signin(response):
    if response.method == 'POST':
        username = response.POST.get('username')
        password = response.POST.get('password')
        user = authenticate(response, username=username, password=password)
        
        if user is not None:
            login(response, user)
            messages.success(response, f"{response.user.username} have logged in successfully!")
            return redirect('home')
        else:
            messages.error(response, "Invalid username or password.")
    
    return render(response, "user/signin.html")

def signout(response):
    username = response.user.username
    logout(response)
    messages.success(response, f"{username} logged out successfully!")
    return redirect('home')

