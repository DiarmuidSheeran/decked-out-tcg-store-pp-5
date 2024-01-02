from django.urls import path
from . import views

urlpatterns = [
	path('', views.landing, name='landing'),
    path('about_us/', views.about_us, name='about_us'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('cookies_policy/', views.cookies_policy, name='cookies_policy'),
    path('news/', views.news, name='news'),
    path('returns_policy/', views.returns_policy, name='returns_policy'),
]