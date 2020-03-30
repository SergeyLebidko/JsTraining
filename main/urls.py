from django.urls import path
from .views import index, fill_base


urlpatterns = [
    path('index/', index, name='index'),
    path('fill_base/', fill_base, name='fill_base')
]
