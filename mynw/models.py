from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class ISUser(AbstractUser):
    """
    ISUser model is enherit from User. More fields are added
    and it is used as authentication model.
    """

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=254)
    email = models.EmailField(max_length=254, unique=True, null=False)
    age = models.PositiveSmallIntegerField()
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