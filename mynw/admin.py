from django.contrib import admin
from .models import ISUser, Idea, Message

# Register your models here.
admin.site.register(ISUser)
admin.site.register(Idea)
admin.site.register(Message)
