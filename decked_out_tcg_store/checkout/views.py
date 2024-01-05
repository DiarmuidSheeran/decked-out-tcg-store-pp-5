from django.shortcuts import render
from cart.cart import Cart

def checkout(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()

    context = {
        "cart_products":cart_products, 
        "quantities":quantities, 
        "totals":totals
    }
    return render(request, "checkout/checkout.html", context)

def order_summary(request):
    return render(request, "checkout/order_summary.html")

