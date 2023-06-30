from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from products.models import Products
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from .models import  CartItem,UserProfile,Order
from products.models import Products
from django.shortcuts import get_object_or_404, redirect
from .models import Cart, Order
from .models import UserProfile
def add_to_cart(request, product_id):
    product = get_object_or_404(Products, pk=product_id)
    user = request.user
    cart, _ = Cart.objects.get_or_create(user=user)

    if product.stock > 0:
        product.stock -= 1
        product.save()
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()

        return redirect('cart') 
    else:
        return redirect('out_of_stock') 


def cart(request):
    cart = Cart.objects.filter(user=request.user).first()
    cart_items = CartItem.objects.filter(cart=cart)

    total_cost = 0
    for item in cart_items:
        total_cost += item.total_price
    
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_cost': total_cost})


def add_cart(request, product_id):
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(user=request.user)
        request.session['cart_id'] = cart.cart_id
    
    product = get_object_or_404(Products, id=product_id)
    
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        if cart_item.quantity < product.stock:
            cart_item.quantity += 1
            cart_item.total_price = cart_item.quantity * product.product_price
            cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,
            total_price=product.product_price,
            cart=cart
        )
        cart_item.save()
    
    return redirect('cart')

def reduce_cart(request, product_id):
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(user=request.user)
        request.session['cart_id'] = cart.cart_id
    
    product = get_object_or_404(Products, id=product_id)
    
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        if cart_item.quantity < product.stock:
            cart_item.quantity -= 1
            cart_item.total_price = cart_item.quantity * product.product_price
            cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,
            total_price=product.product_price,
            cart=cart
        )
        cart_item.save()
    
    return redirect('cart')


def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, cart__user=request.user)
    cart_item.delete()
    return redirect('cart')

def checkout(request):
    return render(request,'checkout.html')


@login_required
def checkout(request):
    user_profile = UserProfile.objects.get(user=request.user)
    cart = Cart.objects.get(user=request.user)

    cart_items = CartItem.objects.filter(cart=cart)

    order = Order.objects.create(user_profile=user_profile, cart=cart)

    order.cart_items.set(cart_items)

    cart_items.delete()

    return redirect('/')



@login_required
def orders(request):
    user_profile = UserProfile.objects.get(user=request.user)
    orders = Order.objects.filter(user_profile=user_profile)
    cart = Cart.objects.get(user=request.user)

    cart_items = CartItem.objects.filter(cart=cart)


    context = {
        'orders': orders,
        'cart_items':cart_items
    }

    return render(request, 'order.html', context)
