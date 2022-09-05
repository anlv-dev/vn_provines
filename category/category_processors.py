from .models import Category

def category_context_processor(request):
    return {
        'all_category': Category.objects.all().order_by('name'),
    }