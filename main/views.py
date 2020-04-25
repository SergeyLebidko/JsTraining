from django.shortcuts import render
from .models import Client, Order, Product


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

