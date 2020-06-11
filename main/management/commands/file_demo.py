import random
import requests
import string
from main.models import Storage
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile

from Crypto.Cipher import AES
from Crypto import Random


BLOCK_SIZE = 16


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
        iv = Random.get_random_bytes(BLOCK_SIZE)
        aes = AES.new(key, AES.MODE_CBC, iv, block_size=BLOCK_SIZE)
        length = BLOCK_SIZE - (len(data) % BLOCK_SIZE)
        data += bytes([length]) * length
        encrypted_data = iv + aes.encrypt(data)

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

            iv = encrypted_data[:BLOCK_SIZE]
            aes = AES.new(key, AES.MODE_CBC, iv, block_size=BLOCK_SIZE)
            decrypted_file_data = aes.decrypt(encrypted_file_data)

            ender_byte = decrypted_file_data[-1]
            decrypted_file_data = decrypted_file_data[:-ender_byte]

            file.write(decrypted_file_data)

        print('Операции завершены...')

