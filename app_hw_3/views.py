from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpRequest

from .models import User, Product, Order


def index(request):
    users = User.objects.all()
    return render(request, 'app_hw_3/index.html', {'users': users})


def get_orders(request, id):
    orders = Order.objects.filter(client_id=id)
    return render(request, 'app_hw_3/orders.html', {'orders': orders})


def get_products(request, order_id):
    orders = Order.objects.get(id=order_id)
    return render(request, 'app_hw_3/order_products.html', {'products': orders.products.all()})
