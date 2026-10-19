from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from .models import Product
from .cart import Cart


def home(request):
    products = Product.objects.filter(
        is_available=True
    ).order_by("-created_at")

    return render(
        request,
        "store/home.html",
        {"products": products}
    )


def product_detail(request, product_id):
    product = get_object_or_404(
        Product,
        id=product_id,
        is_available=True
    )

    return render(
        request,
        "store/product_detail.html",
        {"product": product}
    )
@require_POST
def add_to_cart(request, product_id):
    product = get_object_or_404(
        Product,
        id=product_id,
        is_available=True,
    )

    try:
        quantity = int(request.POST.get("quantity", 1))

        if quantity < 1:
            raise ValueError

        cart = Cart(request)
        cart.add(product, quantity)

    except ValueError:
        request.session["cart_error"] = (
            "Please enter a valid quantity and check available stock."
        )

    return redirect("cart_detail")


def cart_detail(request):
    cart = Cart(request)

    error = request.session.pop("cart_error", None)

    return render(
        request,
        "store/cart_detail.html",
        {
            "cart": cart,
            "error": error,
        },
    )


@require_POST
def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart = Cart(request)
    cart.remove(product)

    return redirect("cart_detail")