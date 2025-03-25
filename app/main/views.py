from calendar import c
from django.http import HttpResponse
from django.shortcuts import render

from products.models import Categories


def index(request):
    categories = Categories.objects.all
    context = {
        "title": "Comp shop - Главная",
        "content": "Главная страница магазина Comp-shop",
        "categories": categories,
    }

    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "Comp shop - о компании",
        "content": "Страница ананас",
        "text_on_page": "Мне люди должны сказать спасибо, что процеССор из моря достал",
    }

    return render(request, "main/about.html", context)
