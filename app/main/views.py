from django.http import HttpResponse
from django.shortcuts import render
from django.template import context


def index(request):
    context = {"title": "Home", "content": "Главная страница магазина home"}

    return render(request, "main/index.html", context)


def about(request):
    return HttpResponse("About page")
