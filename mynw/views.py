from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from . forms import LoginForm, RegistrationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from .models import ISUser

# Create your views here.
class FeedView(View):
    """Return feed.html if user is logged in
    If user is not logged in then redirect to login page"""

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, "mynw/feed.html")
        else:
            return redirect(reverse_lazy("mynw:login"))


def create_user(first_name, last_name, username, email, password, age):
    """Create a new user"""
    user = ISUser(first_name=first_name, last_name=last_name, username=username, email=email, age=age)
    user.set_password(password)
    user.save()
    return user

def login_view(request):
    """If user is already login then redirect to feed page
    If request is POST then check if user is valid"""

    if request.user.is_authenticated:
        messages.info(request, "You are already logged in.")
        return redirect(reverse_lazy("mynw:feed"))

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.login(request)
            if user:
                login(request, user)
                messages.success(request, "Login successfully.")
                return redirect(reverse_lazy("mynw:feed"))
    
    else:
        form = LoginForm()

    return render(request, "home/login.html", {"form": form})

def logout_view(request):
    logout(request)
    messages.info(request, "You are logged out.")
    return redirect(reverse_lazy("mynw:login"))

def register_view(request):
    """If user is not authenticated then render to registration page
    If register then handle the registered informations"""

    if request.user.is_authenticated:
        messages.info(request, "You are already logged in.")
        return redirect(reverse_lazy("mynw:feed"))

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            age = form.cleaned_data["age"]
            user = create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password, age=age)
            login(request, user)
            messages.success(request, "You are registered and logged in.")
            return redirect(reverse_lazy("mynw:feed")) # need to change into edit profile

    else:
        form = RegistrationForm()

    return render(request, "home/registration.html", {"form": form})
