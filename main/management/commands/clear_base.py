from django.core.management.base import BaseCommand
from main.models import Client, Product, Order


class Command(BaseCommand):

    def handle(self, *args, **options):
        Client.objects.all().delete()
        Product.objects.all().delete()
        Order.objects.all().delete()
        print('База данных очищена...')
