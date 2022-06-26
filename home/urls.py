from django.urls import path
from .views import IndexView, FeedView, PostDetailView

app_name="home"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("feed/", FeedView.as_view(), name="feed"),
    path("feed/<str:slug>/", PostDetailView.as_view(), name="post-detail"),
]
