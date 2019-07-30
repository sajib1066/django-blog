from blog.models import Category, Tags

def category_tag(request):
    category = Category.objects.all()
    tag = Tags.objects.all()
    context = {
        'category': category,
        'tag': tag
    }
    return context
