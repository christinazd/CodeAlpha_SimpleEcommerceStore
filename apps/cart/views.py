from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from apps.products.models import Product
from .cart import Cart


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    if quantity > product.stock:
        messages.error(request, f'Only {product.stock} in stock.')
        return redirect('products:product_detail', pk=product_id)
    cart.add(product_id, quantity)
    messages.success(request, f'"{product.name}" added to cart.')
    next_url = request.POST.get('next') or 'products:product_list'
    if next_url == 'cart:cart_detail':
        return redirect('cart:cart_detail')
    if next_url.startswith('/'):
        return redirect(next_url)
    return redirect(next_url)


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product_id)
    messages.success(request, f'"{product.name}" removed from cart.')
    return redirect('cart:cart_detail')


@require_POST
def cart_update(request, product_id):
    cart = Cart(request)
    quantity = int(request.POST.get('quantity', 1))
    product = get_object_or_404(Product, id=product_id)
    if quantity > product.stock:
        messages.error(request, f'Only {product.stock} in stock.')
        return redirect('cart:cart_detail')
    cart.update_quantity(product_id, quantity)
    messages.success(request, 'Cart updated.')
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', {'cart': cart})
