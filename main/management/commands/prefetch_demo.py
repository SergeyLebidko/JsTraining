from django.core.management.base import BaseCommand
from django.db.models import Prefetch
from main.models import Client, Order


class Command(BaseCommand):

    def handle(self, *args, **options):
        pr = Prefetch('order_set', queryset=Order.objects.filter(count__gt=5))
        clients = Client.objects.prefetch_related(pr).all()

        print('\nПеречень клиентов и их заказов более, чем на 5 единиц товара:')
        for client in clients:
            print(client)
            for order in client.order_set.all():
                print(f'  {order}')
