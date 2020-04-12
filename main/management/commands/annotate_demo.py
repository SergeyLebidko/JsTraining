from django.core.management.base import BaseCommand
from main.models import Client, Order, Product
from django.db.models import Count, Sum, Case, When, Value, Q, CharField


class Command(BaseCommand):

    def handle(self, *args, **options):
        """Команда - пример использования annotate в django"""

        # Подсчитаем и выведем количество заказов, сделанных каждым клиентом
        clients = Client.objects.values('title').order_by('title').annotate(orders_count=Count('order'))

        print('\nКоличество заказов, сделанных каждым клиентом')
        for client in clients:
            print(f'{str(client["title"]).rjust(20, " ")} - {client["orders_count"]}')

        # Подсчитаем и выведем количество заказанных товаров
        products = Product.objects.values('title').order_by('title').annotate(products_count=Sum('order__count'))

        print('\nКоличество заказанных единиц каждого товара')
        for product in products:
            print(f'{str(product["title"]).rjust(20, " ")} - {product["products_count"]}')

        # Сводная информация по заказам
        orders = Order.objects.values(
            'client__title',
            'product__title'
        ).order_by(
            'client__title',
            'product__title'
        ).annotate(total_count=Sum('count'))

        print('\nСводная информация по озаказам')
        for order in orders:
            client_title = str(order["client__title"]).ljust(20, " ")
            order_title = str(order["product__title"]).ljust(20, " ")
            total_count = order["total_count"]
            print(f'{client_title} - {order_title} - {total_count}')

        # Счиает количество vip- и не vip-клиентов
        clients = Client.objects.values('vip').order_by('vip').annotate(count=Count('id'))

        print('\nКоличество vip- и не vip-клиентов')
        for client in clients:
            print(f'{"VIP-клиентов: " if client["vip"] else "Не VIP-клиентов: "}{client["count"]}')

        # Использование annotate без функций для вывода кредитного лимита клиентов
        clients = Client.objects.all().annotate(
            description=Case(
                When(credit_limit__gt=5000, then=Value('Большой')),
                When(Q(credit_limit__gt=2000) & Q(credit_limit__lte=5000), then=Value('Средний')),
                default=Value('Маленький'),
                output_field=CharField()
            )
        )

        print('\nКредитные лимиты клиентов')
        for client in clients:
            print(f'{str(client).ljust(20, " ")} - {client.description}')
