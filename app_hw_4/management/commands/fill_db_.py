from django.core.management.base import BaseCommand

from random import randint, choice
from app_hw_4.models import Product, Order, User


class Command(BaseCommand):
    help = 'Create DB content'

    def handle(self, *args, **options):
        for j in ['apple', 'orange', 'juice', 'tea', 'sweets']:
            product = Product(product=j,
                              price=randint(100, 300))
            product.save()
        products_ = Product.objects.all()
        for i in range(1, 6):
            user = User(name=f'User{i}', phone=randint(89840000000, 89849999999))
            user.save()
            for _ in range(3):
                order = Order(client=user)
                order.save()
                for _ in range(1, 3):
                    product = choice(products_)
                    order.products.add(product)
                    order.total_price = order.total_price + product.price
                order.save()
