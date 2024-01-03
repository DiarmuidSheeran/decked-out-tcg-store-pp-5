from django.shortcuts import render
from .models import Product, Category

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    all_categories = Category.objects.all()
    
    selected_category_id = request.GET.get('category')
    if selected_category_id:
        selected_category = Category.objects.get(id=selected_category_id)
        products = Product.objects.filter(categories__in=[selected_category])

    context = {
        'products': products,
        'categories':all_categories,
    }
    return render(request, 'products/product_list.html', context)

def product_detail(request):
    
    return render(request, 'products/product_detail.html')

def product_search(request):
    
    return render(request, 'products/product_search.html')
