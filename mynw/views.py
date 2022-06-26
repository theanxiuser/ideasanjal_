from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from . forms import LoginForm, RegistrationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from .models import ISUser, Message
from django.views.generic import DetailView, UpdateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import EditProfileForm, IdeaCreationForm
from .models import Idea

# Create your views here.

class EditIdeaView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit an idea"""
    model = Idea
    fields = ["title", "description", "category"]
    template_name = "mynw/edit_idea.html"
    context_object_name = "idea"

    def test_func(self):
        """Check if user is the owner of the idea"""
        idea = self.get_object()
        return self.request.user == idea.user


class DeleteIdeaView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete an idea"""

    model = Idea
    sucesses_message = "Idea deleted successfully."
    pk_url_kwarg = "id_number"
    success_url = reverse_lazy("mynw:my-ideas")

    def test_func(self):
        idea = self.get_object()
        return idea.user == self.request.user

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def delete(self, *args, **kwargs):
        messages.success(self.request, self.successes_message)
        super(DeleteIdeaView, self).delete(*args, **kwargs)
        return redirect(self.success_url)


class CreateIdeaView(LoginRequiredMixin, View):
    """Create an idea"""

    template_name = "home/feed.html"
    form_class = IdeaCreationForm

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        idea = form.save(commit=False)
        idea.user = self.request.user
        idea.save()
        messages.success(self.request, "Idea created successfully!")
        return redirect(idea.get_absolute_url())


class MyIdeasView(LoginRequiredMixin, ListView):
    """View for my ideas"""

    def get_queryset(self):
        queryset = Idea.objects.filter(user=self.request.user)
        return queryset

    template_name = "mynw/my_ideas.html"
    context_object_name = "ideas"
    paginate_by = 6


class IdeaView(DetailView, LoginRequiredMixin):
    """Show idea details"""

    model = Idea
    template_name = "mynw/idea.html"
    context_object_name = "idea"
    pk_url_kwarg = "id_number"


class EditProfileView(LoginRequiredMixin, UpdateView):
    """Edit profile view"""

    form = EditProfileForm
    fields = ["first_name", "last_name", "username", "email", "age", "profession", "bio", "skills", "linkedin", "twitter", "facebook", "github"]
    template_name = "mynw/edit_profile.html"
    success_url = reverse_lazy("mynw:profile")
    
    def get_object(self):
        return get_object_or_404(ISUser, pk=self.request.user.id)


class UserProfileView(DetailView):
    """User profile view"""

    model = ISUser
    template_name = "mynw/profile.html"
    context_object_name = "user"
    slug_url_kwarg = "id_number"

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context["self_profile"] = False
        return context


class ProfileView(DetailView):
    """Profile view is used to display own profile"""

    template_name = "mynw/profile.html"
    context_object_name = "user"
    
    def get_object(self):
        return get_object_or_404(ISUser, id=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context["self_profile"] = True
        return context



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
        return redirect(reverse_lazy("home:feed"))

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.login(request)
            if user:
                login(request, user)
                messages.success(request, "Login successfully.")
                return redirect(reverse_lazy("home:feed"))
    
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
        return redirect(reverse_lazy("home:feed"))

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
            return redirect(reverse_lazy("home:feed")) # need to change into edit profile

    else:
        form = RegistrationForm()

    return render(request, "home/registration.html", {"form": form})
