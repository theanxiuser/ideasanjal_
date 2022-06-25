from .import views
from django.urls import path

app_name = "mynw"
urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
    path("feed/", views.FeedView.as_view(), name="feed"),
]