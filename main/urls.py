from django.urls import path
from .views import index, report_1, report_2, simple_rest_report


urlpatterns = [
    path('index/', index, name='index'),
    path('report_1/', report_1, name='report_1'),
    path('report_2/', report_2, name='report_2'),
    path('simple_rest_report/', simple_rest_report, name='simple_rest_report')
]
