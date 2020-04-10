from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from main.utils.transport import send_request


def index(request):
    """Контроллер главной страницы"""
    return render(request, 'main/index.html', {'title': 'Главная страница сайта'})


@api_view(['GET'])
def out_service(request):
    users = send_request()
    result = []
    for user in users:
        result.append(
            {
                'name': user['name'],
                'city': user['address']['city']
            }
        )

    return Response(result)


def show_response():
    print(send_request())
