from django.urls import path
from . import views

urlpatterns = [
	path('account/', views.account, name='account'),
    path('login/', views.user_login, name='login'),
    path('order_history/', views.order_history, name='order_history'),
    path('register/', views.register, name='register'),
    path('update_details/', views.update_details, name='update_details'),
    path('view_details/', views.view_details, name='view_details'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('logout/', views.logoutUser, name="logout"),
    path('admin_panel/', views.admin_panel, name="admin_panel"),
]