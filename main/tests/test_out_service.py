from django.test import TestCase
from rest_framework.test import APIClient
from unittest.mock import patch, Mock
from django.urls import reverse


def fake_request(url):
    print(f'Произошло обращение на URL: {url}')
    response = Mock()
    response.status_code = 200
    response.json.return_value = [
        {
            'name': 'Фейковое имя',
            'address': {
                'city': 'Фейковый город'
            }
        }
    ]
    return response


class OutServiceTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    @patch('main.utils.transport.requests.get', fake_request)
    def test_out_service(self):
        url = reverse('out_service')
        resp = self.client.get(url)

        print(resp.data)
        print(resp.status_code)
        print(type(resp.data))

        print('Тест успешно завершен...')
