from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import get_list_or_404, render
from products.utils import q_search
from products.models import Products


def catalog(request, category_slug=None):

    page = request.GET.get("page", 1)
    on_sale = request.GET.get("on_sale", None)
    order_by = request.GET.get("order_by", None)
    query = request.GET.get("q", None)

    if category_slug == "all":
        products = Products.objects.all()
    elif query.strip():
        products = q_search(query)
    else:
        products = Products.objects.filter(category__slug=category_slug)
        if not products.exists():
            raise Http404("No products found for this category.")

    if on_sale:
        products = products.filter(discount__gt=0)

    if order_by and order_by != "default":
        products = products.order_by(order_by)

    paginator = Paginator(products, 3)

    current_page = paginator.page(int(page))
    context = {
        "title": "Comp-shop catalog",
        "products": current_page,
        "slug_url": category_slug,
    }
    return render(request, "products/catalog.html", context)


def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    context = {
        "product": product,
    }

    return render(request, "products/product.html", context)
