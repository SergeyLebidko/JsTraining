import random
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render

from .models import Client, Order, Product


def index(request):
    """Контроллер главной страницы"""
    return render(request, 'main/index.html', {'title': 'Главная страница сайта'})


@api_view(['POST'])
def fill_base(request):
    client_titles = ['Танос', 'Тони Старк', 'Бэтмен', 'Супермен', 'Капитан Америка', 'Тор', 'Грут']
    product_titles = ['Монитор', 'Жесткий диск', 'Блок питания', 'Видеокарта', 'Процессор', 'Оперативная память']

    for client_title in client_titles:
        Client.objects.create(
            title=client_title,
            credit_limit=random.randint(1000, 10000),
            vip=random.choice([True, False])
        )

    for product_title in product_titles:
        Product.objects.create(
            title=product_title,
            balance=random.randint(100, 1000),
            price=random.randint(500, 5000)
        )

    clients = Client.objects.all()
    products = Product.objects.all()
    for _ in range(20):
        client = random.choice(clients)
        product = random.choice(products)
        Order.objects.create(
            client=client,
            product=product,
            count=random.randint(1, 10)
        )

    return Response(status=status.HTTP_201_CREATED)
