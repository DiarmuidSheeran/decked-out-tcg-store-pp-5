from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.
def account(request):
    
    return render(request, 'user/account.html')

def login(request):
    
    return render(request, 'user/login.html')

def order_history(request):
    
    return render(request, 'user/order_history.html')

def register(request):
    
    return render(request, 'user/register.html')

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
    
    return render(request, 'user/admin_panel.html')