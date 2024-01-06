from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category
from .forms import EditProductForm, CreateProductForm, ProductSearchForm
from cart.cart import Cart
from django.db.models import Q

# Create your views here.
def product_list(request):
    all_categories = Category.objects.all()
    selected_category_ids = request.GET.getlist('categories[]')
    selected_categories = Category.objects.filter(id__in=selected_category_ids)
    products = Product.objects.all()

    for category in selected_categories:
        products = products.filter(categories=category)

    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if min_price and max_price:
        products = products.filter(
            Q(price__range=(min_price, max_price)) | Q(on_special_offer=True, discounted_price__range=(min_price, max_price))
        )
        
    special_offer = request.GET.get('special_offer')
    if special_offer == 'true':
        products = products.filter(on_special_offer=True)

    context = {
        'products': products.distinct(),
        'categories': all_categories,
        'selected_category_ids': selected_category_ids,
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

