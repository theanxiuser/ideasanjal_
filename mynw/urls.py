from cProfile import Profile
from .views import *
from django.urls import path

app_name = "mynw"
urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),
    path("feed/", FeedView.as_view(), name="feed"),

    path("me/", ProfileView.as_view(), name="profile"),
    path("me/edit/", EditProfileView.as_view(), name="edit-profile"),
    path("user/<int:id_number>/", UserProfileView.as_view(), name="user-profile"),
]