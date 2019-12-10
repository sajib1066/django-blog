from blog.models import Category, Tags, MenuCategory, Post
from django.db.models import Count
from contact.forms import NewsletterForm


def mycontext(request):
    tag = Tags.objects.all()
    menu = MenuCategory.objects.all()
    category = Category.objects.all().annotate(number_of_posts=Count('post')).order_by('-number_of_posts', 'name')
    recent_post = Post.objects.filter(is_draft=False).order_by('-id')[:3]
    context = {
        'category': category,
        'tag': tag,
        'menu': menu,
        'posts': recent_post
    }
    return context

def newsletter_form(request):
    forms = NewsletterForm()
    if request.method == 'POST':
        forms = NewsletterForm(request.POST)
        if forms.is_valid():
            forms.save()

    context = {
        'forms': forms
    }
    return context
