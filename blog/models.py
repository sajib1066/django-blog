from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class AuthorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=45)
    author_img = models.ImageField(upload_to='author_images')
    author_description = models.TextField()
    author_facebook = models.URLField(null=True, blank=True)
    author_twitter = models.URLField(null=True, blank=True)
    author_linkedin = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.author_name

class Category(models.Model):
    name = models.CharField(max_length=45, unique=True)
    author = models.ForeignKey(AuthorProfile, on_delete=models.SET_NULL, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Tags(models.Model):
    name = models.CharField(max_length=45, unique=True)
    author = models.ForeignKey(AuthorProfile, on_delete=models.SET_NULL, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='post_images')
    content = RichTextUploadingField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)
    author = models.ForeignKey(AuthorProfile, on_delete=models.SET_NULL, null=True)
    is_draft = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
