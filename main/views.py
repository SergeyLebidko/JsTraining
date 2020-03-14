from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """Контроллер главной страницы"""
    return HttpResponse('Главная страница')
