from django.shortcuts import render

from django.http import HttpResponse, HttpRequest

from .models import User, Product


def index(request):
    users = User.objects.all()
    users_list = '<br>'.join([str(user) for user in users])
    products = Product.objects.all()
    products_list = '<br>'.join([str(product) for product in products])

    return HttpResponse(f'{users_list} <hr> {products_list}')
