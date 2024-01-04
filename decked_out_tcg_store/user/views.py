from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from product.models import Product, Category
from .forms import CreateUserForm
from .models import *

# Create your views here.
def account(request):
    
    return render(request, 'user/account.html')

def login(request):
    
    return render(request, 'user/login.html')

def order_history(request):
    
    return render(request, 'user/order_history.html')

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            fname = form.cleaned_data.get('fname')
            lname = form.cleaned_data.get('lname')
            shipping_address_line_1 = form.cleaned_data.get('shipping_address_line_1')
            shipping_address_line_2 = form.cleaned_data.get('shipping_address_line_2')
            shipping_address_town = form.cleaned_data.get('shipping_address_town')
            shipping_address_county = form.cleaned_data.get('shipping_address_county')
            shipping_address_eircode = form.cleaned_data.get('shipping_address_eircode')
            UserProfile.objects.create(
                user=user,
                fname=fname,
                lname=lname,
                shipping_address_line_1=shipping_address_line_1,
                shipping_address_line_2=shipping_address_line_2,
                shipping_address_town=shipping_address_town,
                shipping_address_county=shipping_address_county,
                shipping_address_eircode=shipping_address_eircode,
            )
            
            return redirect('landing')

    context = {'form': form}
    return render(request, 'user/register.html', context)

def update_details(request):
    
    return render(request, 'user/update_details.html')

def view_details(request):
    
    return render(request, 'user/view_details.html')

def wishlist(request):
    
    return render(request, 'user/wishlist.html')

def logoutUser(request):
  
    logout(request)
    return redirect('landing')

def admin_panel(request):
    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'user/admin_panel.html', context)