from django.shortcuts import render

from blog.models import FeaturedPost, Category, Tags, Post

def home_page(request):
    header_post = FeaturedPost.objects.featured_post()[:2]
    featured_post = FeaturedPost.objects.featured_post()
    recent_post = Post.objects.filter(is_draft=False).order_by('-id')[:6]
    most_read_post = Post.objects.filter(is_draft=False).order_by('-id')[:4]
    context = {
        'header_post': header_post,
        'featured_post': featured_post,
        'recent_post': recent_post,
        'most_read_post': most_read_post
    }
    return render(request, 'home.html', context)

def category_page(request, name):
    category_name = Category.objects.get(name=name)
    ctg_feature_post = Post.objects.filter(category=category_name).order_by('-id')[:2]
    ctg_most_read_post = Post.objects.filter(category=category_name).order_by('-id')[:4]
    post = Post.objects.filter(category=category_name)
    context = {
        'category_name': category_name,
        'ctg_feature_post': ctg_feature_post,
        'ctg_most_read_post': ctg_most_read_post,
        'post': post
    }
    return render(request, 'category.html', context)
