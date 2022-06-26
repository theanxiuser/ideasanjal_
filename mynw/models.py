from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class ISUser(AbstractUser):
    """
    ISUser model is inherit from User. More fields are added
    and it is used as authentication model.
    """

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=254)
    email = models.EmailField(max_length=254, null=False)
    age = models.PositiveSmallIntegerField(null=True)
    profession = models.CharField(max_length=30, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    skills = models.TextField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

# class Idea(models.Model):
#     """
#     Idea model is used to store ideas.
#     """
#
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)
#     category = models.CharField(max_length=20)
#     user = models.ForeignKey(ISUser, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"{self.user} - {self.title}"
#
#     class Meta:
#         verbose_name = "Idea"
#         verbose_name_plural = "Ideas"

class Message(models.Model):
    """Model for messages"""

    sender = models.ForeignKey(ISUser, on_delete=models.CASCADE, related_name="sent_messages")
    receiver = models.ForeignKey(ISUser, on_delete=models.CASCADE, related_name="received_messages")
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    def __str__(self):
        return f"{self.sender} - {self.message}"

