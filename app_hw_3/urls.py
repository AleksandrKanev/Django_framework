from django.urls import path

from .views import index, get_orders, get_products

urlpatterns = [
    path('', index, name='index'),
    path('orders/<int:id>', get_orders, name='get_orders'),
    path('products/<int:order_id>', get_products, name='get_products'),
]
