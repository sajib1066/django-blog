from blog.models import Category, Tags, MenuCategory

def category_tag(request):
    category = Category.objects.all()
    tag = Tags.objects.all()
    menu = MenuCategory.objects.all()
    context = {
        'category': category,
        'tag': tag,
        'menu': menu
    }
    return context
