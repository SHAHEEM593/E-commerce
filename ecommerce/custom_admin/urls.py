from django.urls import path
from . import views

app_name = 'custom_admin'

urlpatterns = [
    path('customs_admin',views.customs_admin,name='customs_admin'),
    path('custom_admin_login',views.custom_admin_login, name='custom_admin_login'),
    path('add_product/', views.add_product, name='add_product'),
]