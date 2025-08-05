from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm


def home(request):
    return "HomePage"

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
            messages.success(request, 'User created')
        else:
            messages.error(request, "Can't create user. Please check the form.")

    else:
        form = CustomUserCreationForm()
    return render(request, 'blog_app/register.html', {'form': form})
