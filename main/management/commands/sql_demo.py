from django.core.management.base import BaseCommand
from django.db import connection


def get_new_cursor():
    return connection.cursor()


def show_results(cursor, description=None, columns=None, fill_count=15):
    if description:
        print(f'\n{description}')

    if columns:
        for column in columns:
            print(column[:fill_count].ljust(fill_count, ' '), end=' ')
        print()

    for line in cursor:
        for element in line:
            print(str(element)[:fill_count].ljust(fill_count, ' '), end=' ')
        print()

    if columns:
        print('-' * (fill_count * len(columns)))
    else:
        print('-' * fill_count)


def client_list():
    # Список клиентов
    cursor = get_new_cursor()
    cursor.execute('SELECT * FROM main_client')
    show_results(
        cursor,
        description='Список клиентов:',
        columns='Идентификатор Клиент Кредитный_лимит VIP-статус'.split(),
        fill_count=15
    )
    cursor.close()


def product_list():
    # Список товаров
    cursor = get_new_cursor()
    cursor.execute('SELECT * FROM main_product')
    show_results(
        cursor,
        description='Список товаров:',
        columns='ИДЕНТИФИКАТОР ТОВАР ОСТАТОК ЦЕНА'.split(),
        fill_count=15
    )
    cursor.close()


def order_list():
    # Список заказов
    cursor = get_new_cursor()
    cursor.execute(
        """SELECT mo.id, mc.title, mp.title, mo.count, mo.count * mp.price as cost
           FROM main_client mc JOIN main_order mo ON mc.id = mo.client_id
           JOIN main_product mp ON mo.product_id = mp.id
           ORDER BY cost"""
    )
    show_results(
        cursor,
        description='Список заказов:',
        columns='ИДЕНТИФИКАТОР КЛИЕНТ ТОВАР КОЛИЧЕСТВО СТОИМОСТЬ_ЗАКАЗА'.split(),
        fill_count=15
    )
    cursor.close()


def report_1():
    # Количество заказанного товара по каждому клиенту
    cursor = get_new_cursor()
    cursor.execute(
        """SELECT mc.title, mp.title, SUM(mo.count) as total_count
           FROM main_client mc JOIN main_order mo
           ON mc.id = mo.client_id JOIN main_product mp 
           ON mp.id = mo.product_id
           GROUP BY mc.title, mp.title
           ORDER BY mc.title, mp.title
        """
    )
    show_results(
        cursor,
        description='Клиенты и количество заказанных товаров:',
        columns='КЛИЕНТ ТОВАР ОБЩЕЕ_КОЛИЧЕСТВО'.split(),
        fill_count=15
    )
    cursor.close()


def report_2():
    # Клиенты, у которых кредитный лимит между 5000 и 9000
    cursor = get_new_cursor()
    cursor.execute('SELECT * FROM main_client WHERE credit_limit BETWEEN 5000 AND 9000')
    show_results(
        cursor,
        description='Клиенты, у которых кредитный лимит между 5000 и 9000:',
        columns='Идентификатор Клиент Кредитный_лимит VIP-статус'.split(),
        fill_count=15
    )
    cursor.close()


def report_3():
    # Клиент и количество его заказов
    cursor = get_new_cursor()
    cursor.execute(
        """SELECT mc.title, COUNT (mo.id)
           FROM main_client mc LEFT JOIN main_order mo 
           ON mc.id = mo.client_id
           GROUP BY mc.title
           ORDER BY mc.title
        """
    )
    show_results(
        cursor,
        description='Клиент и количество его заказов:',
        columns='Клиент Сделано_заказов'.split(),
        fill_count=15
    )
    cursor.close()


def add_test_client():
    # Добавляем нового клиента
    data = {
        't': 'TEST_CLIENT',
        'cl': '5500',
        'v': True
    }
    cursor = get_new_cursor()
    cursor.execute("""INSERT INTO main_client (title, credit_limit, vip) 
                              VALUES (:t, :cl, :v)""", data)
    cursor.close()
    print('\nДобавлен тестовый клиент...\n')


def remove_test_client():
    cursor = get_new_cursor()
    cursor.execute('DELETE FROM main_client WHERE title = "TEST_CLIENT"')
    print('\nУдален тестовый клиент...\n')


class Command(BaseCommand):

    def handle(self, *args, **options):

        add_test_client()
        client_list()
        product_list()
        order_list()
        report_1()
        report_2()
        report_3()

        remove_test_client()
        client_list()
