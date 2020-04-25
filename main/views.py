from django.shortcuts import render


def index(request):
    """Контроллер главной страницы"""
    return render(request, 'main/index.html', {'title': 'Главная страница сайта'})

