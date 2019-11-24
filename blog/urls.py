from django.urls import path
from .views import category, blog_post

urlpatterns = [
    path('category', category, name='category'),
    path('post/<post>', blog_post, name='blog-post')
]
