from django.shortcuts import render
from .models import Client, Order, Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


def index(request):
    """Контроллер главной страницы"""

    clients = Client.objects.all()
    products = Product.objects.all()
    orders = Order.objects.all()

    context = {
        'clients': clients,
        'products': products,
        'orders': orders
    }
    return render(request, 'main/index.html', context=context)


@api_view(['GET'])
def stat(request):
    client_count = Client.objects.all().count()
    product_count = Product.objects.all().count()
    order_count = Order.objects.all().count()

    data = {
        'client_count': client_count,
        'product_count': product_count,
        'order_count': order_count
    }

    return Response(data, status=status.HTTP_200_OK)
