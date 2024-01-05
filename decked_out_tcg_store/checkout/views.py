from django.shortcuts import render, redirect
from cart.cart import Cart
from user.models import UserProfile
from django.contrib.auth.models import User
from order.models import Order, OrderItem
from product.models import Product

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
        order = Order(
            user=request.user if request.user.is_authenticated else None,
            full_name =f"{user_data['fname']} {user_data['lname']}",
            email_address =f"{user_data['email']}",
            shipping_address=f"{shipping_address['line_1']} {shipping_address['line_2']} {shipping_address['town']} {shipping_address['county']} {shipping_address['eircode']}",
            total_price=cart.cart_total(),
        )
        order.save()

        for product_id, quantity in cart.cart.items():
            product = Product.objects.get(pk=product_id)
            price_at_purchase = product.discounted_price if product.on_special_offer else product.price
            order_item = OrderItem(
                order=order,
                product=product,
                quantity=quantity,
                price_at_purchase=price_at_purchase,
            )
            order_item.save()
        
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

