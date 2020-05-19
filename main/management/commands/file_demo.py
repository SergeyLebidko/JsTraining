import random
import requests
import string
from Crypto.Cipher import AES
from main.models import Storage
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile


def get_key():
    random.seed()
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    key = ''.join(random.choice(chars) for _ in range(32))
    return key


class Command(BaseCommand):

    def handle(self, *args, **options):

        storage_list = Storage.objects.all()
        for storage in storage_list:
            storage.pdf_file.delete()
            storage.delete()

        print('Скачиваю файл...')
        url = 'https://www.xeroxscanners.com/downloads/Manuals/XMS/PDF_Converter_Pro_Quick_Reference_Guide.RU.pdf'
        response = requests.get(url)
        data = response.content

        print('Шифрую скачанный файл...')
        key = get_key()
        aes = AES.new(key)
        data = data + b'\x00' * (16 - len(data) % 16)
        encrypted_data = aes.encrypt(data)

        print('Сохраняю скачанный файл в БД...')
        storage = Storage()
        storage.title = 'Демонстрационный файл'
        storage.pdf_file.save('pdf_demo', ContentFile(encrypted_data))
        storage.save()

        print('Получаю сохраненный файл из БД...')
        storage = Storage.objects.get(pk=storage.pk)

        print('Расшифровываю и сохраняю файл из БД на диск...')
        with open('pdf_demo_decrypted.pdf', 'wb') as file:
            encrypted_file_data = storage.pdf_file.read()
            decrypted_file_data = aes.decrypt(encrypted_file_data)
            file.write(decrypted_file_data)

        print('Операции завершены...')

