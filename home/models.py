from django.db import models
from mynw.models import ISUser


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    """ Post model for creating post by admin to show in home"""
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    author = models.ForeignKey(ISUser, on_delete=models.CASCADE)
    image = models.ImageField(default="", upload_to="post-img/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
