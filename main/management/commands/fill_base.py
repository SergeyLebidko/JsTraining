import random
from django.core.management.base import BaseCommand
from main.models import Client, Order, Product


MARVEL = ['Танос', 'Тони Старк', 'Капитан Америка', 'Тор', 'Грут']
DC = ['Бэтмен', 'Супермен']


class Command(BaseCommand):

    def handle(self, *args, **options):
        random.seed()
        client_titles = MARVEL + DC
        product_titles = ['Монитор', 'Жесткий диск', 'Блок питания', 'Видеокарта', 'Процессор', 'Оперативная память']

        print('Удаляю старые данные...')
        Client.objects.all().delete()
        Product.objects.all().delete()

        print('Заполняю таблицу Client...')
        for client_title in client_titles:
            Client.objects.create(
                title=client_title,
                credit_limit=random.randint(1000, 10000),
                vip=random.choice([True, False])
            )

        print('Заполняю таблицу Product...')
        for product_title in product_titles:
            Product.objects.create(
                title=product_title,
                balance=random.randint(100, 1000),
                price=random.randint(500, 5000)
            )

        print('Заполняю таблицу Order...')
        clients = Client.objects.all()
        products = Product.objects.all()
        for _ in range(30):
            client = random.choice(clients)
            product = random.choice(products)
            Order.objects.create(
                client=client,
                product=product,
                count=random.randint(1, 10)
            )

        print('Заполнение завершено...')
