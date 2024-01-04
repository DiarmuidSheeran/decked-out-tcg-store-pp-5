from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category
from .forms import EditProductForm, CreateProductForm, ProductSearchForm
from cart.cart import Cart

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

def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                )
    context = {
        'product': product,
    }

    return render(request,'products/product_detail.html', context)

def product_search(request):
    form = ProductSearchForm(request.GET)
    search_query = form.cleaned_data.get('search_query', '') if form.is_valid() else ''

    if form.is_valid():
        search_query = form.cleaned_data['search_query']
        results = Product.objects.filter(name__icontains=search_query)
    else:
        results = None

    context = {
        'form': form,
        'results': results,
        'search_query': search_query,
    }

    return render(request, 'products/product_search.html', context)

def edit_product(request,  id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                )

    if request.method == 'POST':
        form = EditProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')
    else:
        form = EditProductForm(instance=product)

    context = {
        'product': product,
        'form': form
    }
    return render(request, 'products/edit_product.html', context)

def create_product(request):
    if request.method == 'POST':
        form = CreateProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')
    else:
        form = CreateProductForm()

    context = {
        'form': form
    }
    return render(request, 'products/create_product.html', context)

