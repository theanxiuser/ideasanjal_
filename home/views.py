from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
# from django.contrib import messages

# Create your views here.
class IndexView(View):
    """Return index.html if not logged in, else redirect to feed"""
    def get(self, request):
        if request.user.is_authenticated:
            # messages.info(request, "You are already logged in")
            return redirect(reverse_lazy('mynw:feed'))
        return render(request, "home/index.html")