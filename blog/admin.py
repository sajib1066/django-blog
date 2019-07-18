from django.contrib import admin
from .models import AuthorProfile, Category, Tags, Post, FeaturedPost
# Register your models here.
admin.site.register(AuthorProfile)
admin.site.register(Category)
admin.site.register(Tags)
admin.site.register(Post)
admin.site.register(FeaturedPost)
