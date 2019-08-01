from django.db import models
from django.contrib.auth.models import User

class AuthorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=45)
    author_img = models.ImageField(upload_to='media/author_images')
    author_description = models.TextField()
    gender_choices = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    author_gender = models.CharField(choices=gender_choices, max_length=6)
    author_facebook = models.URLField(null=True, blank=True)
    author_twitter = models.URLField(null=True, blank=True)
    author_linkedin = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.author_name
