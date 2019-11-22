from django.contrib import admin
from .models import Category, Tags, Post, FeaturedPost, MenuCategory

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'title', 'author', 'create_date']

class TagsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'author', 'create_date']

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'author', 'pub_date']

class FeaturedPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'date']

class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'menu', 'date']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(FeaturedPost, FeaturedPostAdmin)
admin.site.register(MenuCategory, MenuCategoryAdmin)
