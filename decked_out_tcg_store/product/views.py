from django.shortcuts import render

# Create your views here.
def product_list(request):
    
    return render(request, 'products/product_list.html')

def product_detail(request):
    
    return render(request, 'products/product_detail.html')

def product_search(request):
    
    return render(request, 'products/product_search.html')
