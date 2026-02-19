from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import Order, OrderItem
from apps.cart.cart import Cart


@login_required
def checkout(request):
    cart = Cart(request)
    if not cart.cart:
        messages.warning(request, 'Your cart is empty.')
        return redirect('products:product_list')
    return render(request, 'orders/checkout.html', {'cart': cart})


@login_required
@require_POST
def place_order(request):
    cart = Cart(request)
    if not cart.cart:
        messages.warning(request, 'Your cart is empty.')
        return redirect('products:product_list')
    order = Order(user=request.user, total_price=cart.get_total_price(), status=Order.STATUS_PENDING)
    order.save()
    for item in cart:
        if item['quantity'] > item['product'].stock:
            messages.error(request, f'Not enough stock for {item["product"].name}.')
            return redirect('orders:checkout')
        OrderItem.objects.create(
            order=order,
            product=item['product'],
            quantity=item['quantity'],
            price=item['price'],
        )
        item['product'].stock -= item['quantity']
        item['product'].save(update_fields=['stock'])
    cart.clear()
    messages.success(request, 'Order placed successfully!')
    return redirect('orders:order_success', order_id=order.id)


@login_required
def order_success(request, order_id):
    order = Order.objects.filter(id=order_id, user=request.user).first()
    if not order:
        messages.error(request, 'Order not found.')
        return redirect('products:product_list')
    return render(request, 'orders/order_success.html', {'order': order})
