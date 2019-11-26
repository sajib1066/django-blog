from django.shortcuts import render
from .models import Post, FeaturedPost

# Create your views here.
def category(request):
    return render(request, 'blog/category.html')

def blog_post(request, post):
    try:
        post = Post.objects.get(id=post)
        most_read_post = Post.objects.filter(is_draft=False).order_by('-id')[:4]
        featured_post = FeaturedPost.objects.featured_post()
        context = {
            'post': post,
            'most_read_post': most_read_post,
            'featured_post': featured_post
        }
        return render(request, 'blog/blog-post.html', context)
    except:
        return render(request, '404.html')

def search_post(request):
    if request.method == 'POST':
        data = request.POST['search']
        posts = Post.objects.filter(title__icontains=data)
        context = {
            'posts': posts
        }
        return render(request, 'blog/search.html', context)
    return render(request, 'blog/search.html')
