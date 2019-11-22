from django.contrib import admin
from .models import Category, Tags, Post, FeaturedPost, MenuCategory

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

admin.site.register(Category)
admin.site.register(Tags)
admin.site.register(Post, PostAdmin)
admin.site.register(FeaturedPost)
admin.site.register(MenuCategory)
