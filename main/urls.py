from django.urls import path
from .views import index, report_1, report_2, simple_rest_report, simple_html_report, add_order, \
    inline_block_demo, modal_demo, simple_template, ajax_demo, ajax_request, dom_demo


urlpatterns = [
    path('index/', index, name='index'),
    path('report_1/', report_1, name='report_1'),
    path('report_2/', report_2, name='report_2'),
    path('simple_rest_report/', simple_rest_report, name='simple_rest_report'),
    path('report_2/simple_html_report/', simple_html_report, name='simple_html_report'),
    path('add_order/', add_order, name='add_order'),
    path('inline_block_demo/', inline_block_demo, name='inline_block_demo'),
    path('modal_demo/', modal_demo, name='modal_demo'),
    path('simple_template/', simple_template, name='simple_template'),
    path('ajax_demo/', ajax_demo, name='ajax_demo'),
    path('ajax_demo/ajax_request/', ajax_request, name='ajax_request'),
    path('dom_demo/', dom_demo, name='dom_demo')
]
