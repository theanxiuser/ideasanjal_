from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, View
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class FeedView(LoginRequiredMixin, View):
    """Return feed.html if user is logged in
    If user is not logged in then redirect to login page"""

    def get(self, request):
        queryset = Post.objects.filter(status=1).order_by('-created_at')
        ctx = {"post_list": queryset}
        return render(request, "home/feed.html", ctx)


class PostDetailView(LoginRequiredMixin, DetailView):
    """Detail of post"""
    model = Post
    template_name = "home/post_detail.html"


class IndexView(View):
    """Return index.html if not logged in, else redirect to feed"""
    def get(self, request):
        if request.user.is_authenticated:
            # messages.info(request, "You are already logged in")
            return redirect(reverse_lazy('home:feed'))
        return render(request, "home/home.html")

