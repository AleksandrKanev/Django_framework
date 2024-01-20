from django.core.management.base import BaseCommand

from app_hw_2.models import Product


class Command(BaseCommand):
    help = 'Create product'

    def handle(self, *args, **options):
        product = Product(product='Apple')
        product.save()