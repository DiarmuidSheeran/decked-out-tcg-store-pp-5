from django.shortcuts import render, get_object_or_404
from product.models import Product
from .cart import Cart
from django.http import JsonResponse

# Create your views here.
def cart_summary(request):

    return render(request, "cart/cart_summary.html")

def cart_add(request):

    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=product_qty)

        cart_quantity = cart.__len__()

        response = JsonResponse({'qty': cart_quantity})
        return response

def cart_delete(request):
   pass

def cart_update(request):

    pass