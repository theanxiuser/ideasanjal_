from .views import *
from django.urls import path

app_name = "mynw"
urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),

    path("me/", ProfileView.as_view(), name="profile"),
    path("me/edit/", EditProfileView.as_view(), name="edit-profile"),
    path("user/<int:id_number>/", UserProfileView.as_view(), name="user-profile"),

    # path("idea/<int:id_number>", IdeaView.as_view(), name="idea"),
    
    # path("me/ideas/", MyIdeasView.as_view(), name="my-ideas"),
    # path("me/ideas/delete/<int:id_number>", DeleteIdeaView.as_view(), name="delete-idea"),
    # path("me/ideas/create/", CreateIdeaView.as_view(), name="create-idea"),
    # path("me/ideas/edit/<int:id_number>/", EditIdeaView.as_view(), name="edit-idea")
]