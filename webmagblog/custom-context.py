from blog.models import Category, Tags, MenuCategory
from django.db.models import Count


def mycontext(request):
    tag = Tags.objects.all()
    menu = MenuCategory.objects.all()
    category = Category.objects.all().annotate(number_of_posts=Count('post')).order_by('-number_of_posts', 'name')

    context = {
        'category': category,
        'tag': tag,
        'menu': menu
    }
    return context
