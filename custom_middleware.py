from django.utils.deprecation import MiddlewareMixin


class FirstCustomMiddleware(MiddlewareMixin):

    def process_request(self, request):
        print(f'Вызван process_request {self.__class__.__name__}')

    def process_view(self, request, view, *args, **kwargs):
        print(f'Вызван process_view {self.__class__.__name__}. View {view.__name__}')

    def process_exception(self, request, exception):
        print(f'Вызван process_exception {self.__class__.__name__}')

    def process_template_response(self, request, template_response):
        print(f'Вызван process_template_response {self.__class__.__name__}')
        template_response.context_data.update({'first_mid_name': self.__class__.__name__})
        return template_response

    def process_response(self, request, response):
        print(f'Вызван process_response {self.__class__.__name__}. Тип response {type(response)}')
        return response


class SecondCustomMiddleware(MiddlewareMixin):

    def process_request(self, request):
        print(f'Вызван process_request {self.__class__.__name__}')

    def process_view(self, request, view, *args, **kwargs):
        print(f'Вызван process_view {self.__class__.__name__}. View {view.__name__}')

    def process_exception(self, request, exception):
        print(f'Вызван process_exception {self.__class__.__name__}')

    def process_template_response(self, request, template_response):
        print(f'Вызван process_template_response {self.__class__.__name__}')
        template_response.context_data.update({'second_mid_name': self.__class__.__name__})
        return template_response

    def process_response(self, request, response):
        print(f'Вызван process_response {self.__class__.__name__}. Тип response {type(response)}')
        return response


def func_middleware(get_response):

    def mid(request):
        print('Внутри посредника-функции до получения response')
        response = get_response(request)
        print('Внутри посредника-функции после получения response')
        return response

    return mid
