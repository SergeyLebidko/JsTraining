from django.test import TestCase
from rest_framework.test import APIClient
from unittest.mock import patch
from django.urls import reverse


def fake_request():
    return [{'name': 'Фейковое имя', 'address': {'city': 'Фейковый город'}}]


class OutServiceTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    @patch('main.views.send_request', fake_request)
    def test_out_service(self):
        url = reverse('out_service')
        resp = self.client.get(url)

        print(resp.data)
        print(resp.status_code)
        print(type(resp.data))

        print('Тест успешно завершен...')
