from django.urls import path
from . import views

urlpatterns = [
	path('product_list/', views.product_list, name='product_list'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('product_search/', views.product_search, name='product_search'),
]