from django.shortcuts import render

from blog.models import FeaturedPost, Category, Tags, Post

def home_page(request):
    header_post = FeaturedPost.objects.featured_post()[:2]
    featured_post = FeaturedPost.objects.featured_post()
    post = Post.objects.all()
    context = {
        'header_post': header_post,
        'featured_post': featured_post,
        'post': post
    }
    return render(request, 'home.html', context)
