from django.shortcuts import render

# Create your views here.
def landing(request):
    
    return render(request, 'landing.html')

def about_us(request):
    
    return render(request, 'about_us.html')

def contact_us(request):
    
    return render(request, 'contact_us.html')

def cookies_policy(request):
    
    return render(request, 'cookies_policy.html')

def news(request):
    
    return render(request, 'news.html')

def returns_policy(request):
    
    return render(request, 'returns_policy.html')