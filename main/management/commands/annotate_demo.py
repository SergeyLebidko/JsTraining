from django.core.management.base import BaseCommand
from main.models import Client, Order, Product
from django.db.models import Sum, Case, When, Value, CharField
from django.db import connection


class Command(BaseCommand):

    def handle(self, *args, **options):
        # orders = Order.objects.values(
        #     'product__title'
        # ).order_by('product__title').annotate(cnt=Count('product'))

        orders = Order.objects.values(
            'product__title'
        ).order_by(
            'product'
        ).annotate(
            cnt=Sum('count'),
            description=Case(When(cnt__gt=20, then=Value('Много')), default=Value('Мало'), output_field=CharField())
        )

        print('\nРезультат запроса:')
        for order in orders:
            print(order)

        print('\nSQL:')
        for sql in connection.queries:
            print(sql)
