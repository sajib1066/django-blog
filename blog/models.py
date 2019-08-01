from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

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

class Category(models.Model):
    name = models.CharField(max_length=45, unique=True)
    author = models.ForeignKey(AuthorProfile, on_delete=models.SET_NULL, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s by %s' % (self.name, self.author)

class Tags(models.Model):
    name = models.CharField(max_length=45, unique=True)
    author = models.ForeignKey(AuthorProfile, on_delete=models.SET_NULL, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class PostManager(models.Manager):
    def latest_post(self):
        l_post = Post.objects.filter(is_draft=False).order_by('-pub_date')[:3]
        return l_post

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='media/post_images')
    content = RichTextUploadingField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)
    author = models.ForeignKey(AuthorProfile, on_delete=models.SET_NULL, null=True)
    is_draft = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now_add=True)

    objects = PostManager()

    def __str__(self):
        return self.title

class FeaturedPostManager(models.Manager):
    def featured_post(self):
        f_post = FeaturedPost.objects.filter(is_draft=False).order_by('-date')[:2]
        return f_post

class FeaturedPost(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    is_draft = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    objects = FeaturedPostManager()

    def __str__(self):
        return str(self.post)
