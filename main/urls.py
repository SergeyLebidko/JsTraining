from django.urls import path
from .views import index, out_service


urlpatterns = [
    path('index/', index, name='index'),
    path('out_service/', out_service, name='out_service')
]
