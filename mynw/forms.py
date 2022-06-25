from django import forms
from .models import ISUser
from django.contrib.auth import authenticate

class EditProfileForm(forms.ModelForm):
    class Meta:
        fields = ["first_name", "last_name", "username", "email", "age", "profession", "bio", "skills", "linkedin", "twitter", "facebook", "github"]

class RegistrationForm(forms.ModelForm):
    """RegistrationForm is used to register a new user."""
    
    class Meta:
        model = ISUser
        fields = ["first_name", "last_name", "username", "email", "password", "age"]
        order = fields

        def __init__(self, *args, **kwargs):
            super(RegistrationForm, self).__init__(*args, **kwargs)
            self.fields["password"].widget = forms.PasswordInput()

        def clean_username(self):
            """Check if username is unique."""
            username = self.cleaned_data["username"]
            if ISUser.objects.filter(username=username).exists():
                raise forms.ValidationError("This username has already been taken.")
            return username

class LoginForm(forms.Form):
    """LoginForm is used to login a user."""

    username = forms.CharField(label="Username", max_length=20, min_length=5, widget=forms.TextInput(attrs={"placeholder": "Username"}))

    password = forms.CharField(label="Password", max_length=30, widget=forms.PasswordInput(attrs={"placeholder": "Password"}))

    def clean(self):
        """Check if user is valid."""
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Invalid username or password.")
        return self.cleaned_data
    
    def login(self, request):
        """Login a user."""
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        return user