from django.shortcuts import render, redirect
from product.models import Product
from cart.models import Cart, CartItem

# Create your views here.

def _thong_tin_cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def them_vao_gio_hang(request, product_id):
    product = Product.objects.get(id=product_id)
    # Them vao Cart model
    try:
        cart = Cart.objects.get(cart_id = _thong_tin_cart_id(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(cart_id = _thong_tin_cart_id(request))
    cart.save()

    # Them vao CartItem Model
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=product, quantity = 1, cart=cart)
        cart_item.save()
    # return HttpResponse(cart_item.product)
    return redirect('cart:cart')

def xoa_khoi_gio_hang(request, product_id):
    product = Product.objects.get(id=product_id)
    # Them vao Cart model
    try:
        cart = Cart.objects.get(cart_id = _thong_tin_cart_id(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(cart_id = _thong_tin_cart_id(request))
    cart.save()

    # Them vao CartItem Model
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        if cart_item.quantity >=1:
            cart_item.quantity -= 1
            cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=product, quantity = 1, cart=cart)
        cart_item.save()
    # return HttpResponse(cart_item.product)
    return redirect('cart:cart')


def gio_hang(request, total=0, quantity=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id = _thong_tin_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity )
            quantity += cart_item.quantity
    except Cart.DoesNotExist:
        pass
    
    tax = (total*10)/100
    total_order = total + tax
    context = {
        'total': total,
        'quantity': quantity,
        'tax': tax,
        'total_order': total_order,
        'cart_items': cart_items,
    }
    return render(request,'my_tmp/cart.html',context)

def check_out(request,total=0, quantity=0, cart_items=None):
    context={}
    
    try:
        cart = Cart.objects.get(cart_id = _thong_tin_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity )
            quantity += cart_item.quantity
    except Cart.DoesNotExist:
        pass
    
    #tax = (total*10)/100
    #total_order = total + tax
    context = {
        'total': total,
        #'quantity': quantity,
        #'tax': tax,
        #'total_order': total_order,
        'cart_items': cart_items,
    }
    return render(request,'my_tmp/place-order.html',context)
