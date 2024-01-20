from django.core.management.base import BaseCommand

from app_hw_2.models import User


class Command(BaseCommand):
    help = 'Create user'

    def handle(self, *args, **options):
        user = User(name='Alex', phone=123)
        user.save()
