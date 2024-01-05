from django.shortcuts import render, redirect
from cart.cart import Cart
from user.models import UserProfile
from django.contrib.auth.models import User
from order.models import Order, OrderItem
from product.models import Product
from .forms import CheckoutForm
from django.conf import settings
from django.http import JsonResponse
import stripe
from django.views.decorators.csrf import csrf_exempt

# views.py
from django.shortcuts import render, redirect
from cart.cart import Cart
from user.models import UserProfile
from django.contrib.auth.models import User
from order.models import Order, OrderItem
from product.models import Product
from .forms import CheckoutForm
from django.conf import settings

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
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY
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

@csrf_exempt
def create_checkout_session(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    cart = Cart(request)
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'eur',
                    'product_data': {
                        'name': 'Your Product',
                    },
                    'unit_amount': int(cart.cart_total() * 100),  # Amount in cents
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri('/success/'),
            cancel_url=request.build_absolute_uri('/cancel/'),
        )

        return JsonResponse({'id': session.id})
    except stripe.error.StripeError as e:
        return JsonResponse({'error': str(e)}, status=402)

