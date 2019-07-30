from django.shortcuts import render

from .models import Post
# Create your views here.
def category(request):
    return render(request, 'blog/category.html')

def blog_post(request, post):
    post = Post.objects.get(id=post)
    context = {'post': post}
    return render(request, 'blog/blog-post.html', context)
