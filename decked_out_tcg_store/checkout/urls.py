from django.urls import path
from . import views

urlpatterns = [
	path('checkout/', views.checkout, name='checkout'),
    path('order_summary/', views.order_summary, name='order_summary'),
    path('create_checkout_session/', views.create_checkout_session, name='create_checkout_session'),
]