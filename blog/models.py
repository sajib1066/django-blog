from django.db import models
# from urllib import request
from django.conf import settings
from administration.models import Profile
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=45)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
