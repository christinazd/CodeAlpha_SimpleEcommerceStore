def cart_total(request):
    from .cart import Cart
    cart = Cart(request)
    return {
        'cart_total_items': len(cart),
        'cart_total_price': cart.get_total_price(),
    }
