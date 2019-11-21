from blog.models import Category, Tags, MenuCategory

def category_tag(request):
    category = Category.objects.all().order_by('name')
    tag = Tags.objects.all()
    menu = MenuCategory.objects.all()
    context = {
        'category': category,
        'tag': tag,
        'menu': menu
    }
    return context
