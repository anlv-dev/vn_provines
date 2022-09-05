from django.shortcuts import render
from product.models import Product
from category.models import Category
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def trang_chu(request):
    #all_cat = Category.objects.all()
    products = Product.objects.filter(is_available=True).order_by('name')
    context = {
        "products": products,
        #"all_cat": all_cat
    }
    # my_app/templates/my_tmp/index.html
    return render(request, 'my_tmp/index.html', context)

def trang_search(request):
    #all_cat = Category.objects.all()
    if request.method == 'POST':
        search_text = request.POST["q"]
        print(search_text)
        #first_name = request.POST["first_name"]
        products = Product.objects.filter(Q(name__icontains=search_text) | Q(description__icontains=search_text)).order_by('name')
        context = {
            "products": products,         
        }
        return render(request, 'my_tmp/search.html', context)

def trang_store(request, slug=None):
    all_cat = Category.objects.all()

    if slug:
        products = Product.objects.filter(category__slug=slug).filter(is_available=True).order_by('name')
        #Article.objects.filter(reporter__first_name='John')
        totalItems = Product.objects.filter(category__slug=slug).filter(is_available=True).count()
    else:
        totalItems = Product.objects.filter(is_available=True).count()
        products = Product.objects.filter(is_available=True).order_by('name')
    
    #Pagination
    paginator = Paginator(products, 6) # Show 2 items in a page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    loop_page = range(1, paginator.num_pages)

    context = {
        "totalItems" : totalItems,
        "products" : products,
        "all_cat": all_cat,
        "page_obj" : page_obj,
        "loop_page" : loop_page,

    }
    return render(request, 'my_tmp/store.html', context)


def product_detail(request,slug):
    product = Product.objects.get(slug=slug)
    print(slug)
    context = {
        "product":product
    }
    return render(request,'my_tmp/product-detail.html',context)

