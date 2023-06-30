from django.shortcuts import render,redirect
from .models import Products
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
def products(request):
    product=Products.objects.all()
    context={
        'product':product
    }
    return render(request,'products.html',context)
