from django.shortcuts import render
from django.http import HttpResponse
from blog.models import FeaturedPost, Category, Tags, Post

def error_404(request, allowed_hosts=True):
    data = {'message': '404 - Page not found'}
    return render(request, 'error.html', data)

def error_500(request, allowed_hosts=True):
    data = {'message': '500 Internal Server Error'}
    return render(request, 'error.html', data)

def home_page(request):
    try:
        header_post = FeaturedPost.objects.featured_post()[:2]
        featured_post = FeaturedPost.objects.featured_post()
        recent_post = Post.objects.filter(is_draft=False).order_by('-id')[:6]
        most_read_post = Post.objects.filter(is_draft=False).order_by('-id')[:4]
        context = {
            'header_post': header_post,
            'featured_post': featured_post,
            'recent_post': recent_post,
            'most_read_post': most_read_post,
            'post': recent_post[2]
        }
        return render(request, 'home.html', context)
    except Exception:
        return HttpResponse(
            """
                <h2>Please add some blog from admin panel</h2>
                <a href="admin">Admin Panel</a>
            """
        )

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

def about_page(request):
    most_read_post = Post.objects.filter(is_draft=False).order_by('-id')[:4]
    context = {
        'most_read_post': most_read_post
    }
    return render(request, 'about.html', context)
