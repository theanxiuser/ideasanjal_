from django.urls import path
from .views import IndexView, FeedView, PostDetailView

app_name="home"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("home/", FeedView.as_view(), name="feed"),
    path("home/<str:slug>/", PostDetailView.as_view(), name="post-detail"),
]
