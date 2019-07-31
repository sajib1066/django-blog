from django.shortcuts import render

from blog.models import FeaturedPost, Category, Tags, Post

def home_page(request):
    featured_post = FeaturedPost.objects.all()
    post = Post.objects.all()
    context = {
        'featured_post': featured_post,
        'post': post
    }
    return render(request, 'home.html', context)
