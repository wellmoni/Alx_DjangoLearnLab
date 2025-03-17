from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

# User Registration
def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")  
    else:
        form = CustomUserCreationForm()
    return render(request, "blog/register.html", {"form": form})

# User Login
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("profile")
    else:
        form = AuthenticationForm()
    return render(request, "blog/login.html", {"form": form})

# User Logout
def logout_view(request):
    logout(request)
    return redirect("login")

# Profile Management
@login_required
def profile_view(request):
    return render(request, "blog/profile.html", {"user": request.user})
from .models import Profile
from django.contrib.auth.forms import UserChangeForm

@login_required
def profile_view(request):
    if request.method == "POST":
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, "blog/profile.html", {"form": form})



# Create your views here.
