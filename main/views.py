from django.shortcuts import render
from .models import Client, Order, Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.template.loader import get_template

stat_counter = 0


def index(request):
    return render(request, 'main/index.html', context={})


def report_1(request):
    clients = Client.objects.all()
    products = Product.objects.all()
    orders = Order.objects.all()

    context = {
        'clients': clients,
        'products': products,
        'orders': orders,
    }
    return render(request, 'main/report_1.html', context=context)


def report_2(request):
    return render(request, 'main/report_2.html', context={})


def simple_html_report(request):
    # Количество клиентов/товаров/заказов
    clients_count = Client.objects.count()
    products_count = Product.objects.count()
    orders_count = Order.objects.count()

    context = {
        'clients_count': clients_count,
        'products_count': products_count,
        'orders_count': orders_count
    }
    template = get_template('main/html_report_template.html')
    return HttpResponse(template.render(context=context, request=request))


@api_view(['GET'])
def simple_rest_report(request):
    client_count = Client.objects.all().count()
    product_count = Product.objects.all().count()
    order_count = Order.objects.all().count()

    global stat_counter
    stat_counter += 1

    data = {
        'stat': {
            'client_count': client_count,
            'product_count': product_count,
            'order_count': order_count,
            'stat_counter': stat_counter
        },
        'description': {
            'client_count': 'Количество клиентов',
            'product_count': 'Количество товаров',
            'order_count': 'Количество заказов',
            'stat_counter': 'Запросов статистики'
        }

    }
    return Response(data, status=status.HTTP_200_OK)
