from django.urls import path
from . import views

urlpatterns = [
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('reduce_cart/<int:product_id>/', views.reduce_cart, name='reduce_cart'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('order/', views.orders, name='order'),

]
