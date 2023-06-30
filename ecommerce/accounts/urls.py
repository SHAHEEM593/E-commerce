from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.index,name='home'),
    path('signup/',views.signup, name='signup'),
    path('login',views.user_login, name='login'),
    path('logout',views.user_logout, name='logout'),
    path('newhome',views.newhome,name='newhome'),
]
