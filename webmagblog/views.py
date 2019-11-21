from django.shortcuts import render

from blog.models import FeaturedPost, Category, Tags, Post

def home_page(request):
    header_post = FeaturedPost.objects.featured_post()[:2]
    featured_post = FeaturedPost.objects.featured_post()
    recent_post = Post.objects.filter(is_draft=False).order_by('-id')[:6]
    context = {
        'header_post': header_post,
        'featured_post': featured_post,
        'recent_post': recent_post
    }
    return render(request, 'home.html', context)

def category_page(request):
    return render(request, 'category.html')
