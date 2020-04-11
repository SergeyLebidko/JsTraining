from django.core.management.base import BaseCommand
from main.models import Client, Order, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        clients = Client.objects.all()
        products = Product.objects.all()
        orders = Order.objects.all()

        print(f'\n{"-" * 15} Клиенты {"-" * 15}')
        for number, client in enumerate(clients, 1):
            print(f'{number}. {client}')

        print(f'\n{"-" * 15} Товары {"-" * 15}')
        for number, product in enumerate(products, 1):
            print(f'{number}. {product}')

        print(f'\n{"-" * 15} Заказы {"-" * 15}')
        for number, order in enumerate(orders, 1):
            print(f'{str(number).rjust(2, " ")}. {order}')
