from django.shortcuts import render

from blog.models import FeaturedPost, Category, Tags, Post

def home_page(request):
    category = Category.objects.all()
    tag = Tags.objects.all()
    featured_post = FeaturedPost.objects.featured_post()
    post = Post.objects.all()
    context = {
        'featured_post': featured_post,
        'category': category,
        'tag': tag,
        'post': post
    }
    return render(request, 'home.html', context)
