from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from .forms import CustomUserCreationForm,CustomLoginForm


def home(request):
    return render(request, 'blog_app/home.html')

def register_user(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=raw_password)
            if user is not None:
                login(request, user)
                messages.success(request, 'User created and logged in!')
                return redirect('home')  
        else:
            messages.error(request, "Can't create user. Please check the form.")

    else:
        form = CustomUserCreationForm()
    return render(request, 'blog_app/register.html', {'form': form})

def login_user(request):
    if request.method == "POST":
        form = CustomLoginForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            messages.success(request, 'Login successful.')
            return redirect('home')  
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = CustomLoginForm()

    return render(request, 'blog_app/login.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.error(request, 'You have been logged out successfully.')
    redirect('login')