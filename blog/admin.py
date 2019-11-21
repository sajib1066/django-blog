from django.contrib import admin
from .models import Category, Tags, Post, FeaturedPost, MenuCategory

admin.site.register(Category)
admin.site.register(Tags)
admin.site.register(Post)
admin.site.register(FeaturedPost)
admin.site.register(MenuCategory)
