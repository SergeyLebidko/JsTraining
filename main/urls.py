from django.urls import path
from .views import index, stat


urlpatterns = [
    path('index/', index, name='index'),
    path('stat/', stat, name='stat')
]
