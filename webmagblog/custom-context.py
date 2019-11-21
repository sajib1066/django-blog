from blog.models import Category, Tags

def category_tag(request):
    category = Category.objects.all()
    tag = Tags.objects.all()
    menu = Category.objects.all()[:4]
    context = {
        'category': category,
        'tag': tag,
        'menu': menu
    }
    return context
