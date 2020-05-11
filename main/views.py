from django.shortcuts import render
from .models import Client, Order, Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, HttpResponseNotAllowed
from django.template.loader import get_template
from django.db.models import Sum, F


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


def add_order(request):
    if request.method == 'GET':
        clients = Client.objects.all()
        products = Product.objects.all()
        context = {
            'clients': clients,
            'products': products
        }
        return render(request, 'main/add_order.html', context=context)
    elif request.method == 'POST':
        client_id = request.POST.get('client_id')
        product_id = request.POST.get('product_id')
        count = request.POST.get('count')
        Order.objects.create(
            product_id=product_id,
            client_id=client_id,
            count=count
        )
        return HttpResponse('Заказ успешно добавлен')

    return HttpResponseNotAllowed(['GET', 'POST'])


def simple_html_report(request):
    # Количество клиентов/товаров/заказов
    clients_count = Client.objects.count()
    products_count = Product.objects.count()
    orders_count = Order.objects.count()

    # Клиенты, количество заказанных ими товаров и их стоимость
    order_report = Order.objects.values(
        'client__title',
        'product__title'
    ).order_by(
        'client__title',
        'product__title'
    ).annotate(product_count=Sum('count'), total_cost=Sum(F('count')*F('product__price')))

    global stat_counter
    stat_counter += 1

    context = {
        'clients_count': clients_count,
        'products_count': products_count,
        'orders_count': orders_count,
        'order_report': order_report,
        'stat_counter': stat_counter
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


def inline_block_demo(request):
    return render(request, 'main/inline_block_demo.html', context={})


def modal_demo(request):
    return render(request, 'main/modal_demo.html', context={})
