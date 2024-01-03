from django.shortcuts import render
from .models import Product

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    
    context = {
        'products': products,
    }
    return render(request, 'products/product_list.html', context)

def product_detail(request):
    
    return render(request, 'products/product_detail.html')

def product_search(request):
    
    return render(request, 'products/product_search.html')
