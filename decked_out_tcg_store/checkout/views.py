from django.shortcuts import render, redirect
from cart.cart import Cart
from user.models import UserProfile
from django.contrib.auth.models import User

def checkout(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()
    user = request.user

    shipping_address = {
        'line_1': '',
        'line_2': '',
        'town': '',
        'county': '',
        'eircode': '',
    }

    user_data = {
        'fname': '',
        'lname': '',
        'email': '',
    }

    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        shipping_address = {
            'line_1': user_profile.shipping_address_line_1,
            'line_2': user_profile.shipping_address_line_2,
            'town': user_profile.shipping_address_town,
            'county': user_profile.shipping_address_county,
            'eircode': user_profile.shipping_address_eircode,
        }
        user_data = {
            'fname': user_profile.fname,
            'lname': user_profile.lname,
            'email': user.email,
        }

    if request.method == 'POST':
        cart.clear()
        return redirect('order_summary')

    context = {
        "cart_products":cart_products, 
        "quantities":quantities, 
        "totals":totals,
        'shipping_address': shipping_address,
        'user_data': user_data,
    }
    return render(request, "checkout/checkout.html", context)

def order_summary(request):
    return render(request, "checkout/order_summary.html")

