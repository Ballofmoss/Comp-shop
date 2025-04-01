from gc import get_objects
from django.shortcuts import get_list_or_404, render
from products.models import Products


def catalog(request, category_slug):
    if category_slug == "all":
        products = Products.objects.all()
    else:
        products = get_list_or_404(
            Products.objects.filter(category__slug=category_slug)
        )
    context = {
        "title": "Comp-shop catalog",
        "products": products,
    }
    return render(request, "products/catalog.html", context)


def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    context = {
        "product": product,
    }

    return render(request, "products/product.html", context)
