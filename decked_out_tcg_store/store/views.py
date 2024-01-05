from django.shortcuts import render
from .models import SlideshowImage
from user.models import UserProfile
# Create your views here.
def landing(request):
    slideshow_images = SlideshowImage.objects.all()

    context = {
        'slideshow_images': slideshow_images
    }

    return render(request, 'landing.html', context)

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