from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from product.models import Product, Category
from .forms import CreateUserForm, UpdateForm
from .models import *
from django.contrib.auth.models import User


# Create your views here.
def account(request):
    
    return render(request, 'user/account.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('landing')

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
    user = request.user
    profile = UserProfile.objects.get(user=user)

    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.fname = form.cleaned_data.get('fname')
            profile.lname = form.cleaned_data.get('lname')
            profile.shipping_address_line_1 = form.cleaned_data.get('shipping_address_line_1')
            profile.shipping_address_line_2 = form.cleaned_data.get('shipping_address_line_2')
            profile.shipping_address_town = form.cleaned_data.get('shipping_address_town')
            profile.shipping_address_county = form.cleaned_data.get('shipping_address_county')
            profile.shipping_address_eircode = form.cleaned_data.get('shipping_address_eircode')
            profile.save()
            return redirect('account')
    else:
        form = UpdateForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'user/update_details.html', context)

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