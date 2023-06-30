from django.shortcuts import render, redirect
from .forms import AddProductForm, UpdateQuantityForm
from products .models import Products
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate, login
from .forms import LoginForms
from django.views.decorators.csrf import csrf_protect
@csrf_protect
def custom_admin_login(request):
    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_superuser:
                login(request, user)
                return redirect('newhome')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForms()
    return render(request, 'custom_admin_login.html', {'form': form})

def customs_admin(request):
    return render(request,'custom_admin.html')

def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = AddProductForm()
    return render(request, 'add_product.html', {'form': form})


