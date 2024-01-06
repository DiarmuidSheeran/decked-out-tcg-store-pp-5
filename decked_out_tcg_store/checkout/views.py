from django.shortcuts import render, redirect
from cart.cart import Cart
from user.models import UserProfile
from django.contrib.auth.models import User
from order.models import Order, OrderItem
from product.models import Product
from .forms import CheckoutForm
from django.conf import settings
from django.http import JsonResponse

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

    else:
        user = None
        form = CheckoutForm(request.POST)
        if form.is_valid():
            shipping_address = {
                'line_1': form.cleaned_data.get('shipping_address_line_1'),
                'line_2': form.cleaned_data.get('shipping_address_line_2'),
                'town': form.cleaned_data.get('shipping_address_town'),
                'county': form.cleaned_data.get('shipping_address_county'),
                'eircode': form.cleaned_data.get('shipping_address_eircode'),
            }
            user_data = {
                'fname': form.cleaned_data.get('fname'),
                'lname': form.cleaned_data.get('lname'),
                'email': form.cleaned_data.get('email'),
            }

    context = {
        "cart_products": cart_products,
        "quantities": quantities,
        "totals": totals,
        'shipping_address': shipping_address,
        'user_data': user_data,
    }
    return render(request, "checkout/checkout.html", context)

def order_summary(request):
    latest_order = None
    if request.user.is_authenticated:
        latest_order = Order.objects.filter(user=request.user).order_by('-created_at').first()
    if not latest_order:
        latest_order = Order.objects.filter(user=None).order_by('-created_at').first()

    context = {'latest_order': latest_order}
    return render(request, "checkout/order_summary.html", context)

