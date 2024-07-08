import datetime

from gspread import Client, service_account
from bot_settings import config

table_link = config.table_link


async def client_init_json():
    """Создание клиента для работы с Google Sheets."""

    # JSON файл для доступа
    return service_account(filename=r'test-tg-proj.json')


async def get_table_by_url(client: Client, table_url):
    """Получение таблицы из Google Sheets по ссылке."""

    return client.open_by_url(table_url)


async def get_data():
    """Извлечение данных из ячейки А2 таблицы"""

    client = await client_init_json()
    table = await get_table_by_url(client, table_link)
    data = table.sheet1.acell('A2').value
    return data


async def add_data(input_date):
    """Добавление данных в ячейки столбца В"""

    client = await client_init_json()
    table = await get_table_by_url(client, table_link)

    # проверка формата даты на соответствие дд.мм.гггг
    try:
        date_format = "%d.%m.%Y"
        datetime.datetime.strptime(str(input_date), date_format)
    except ValueError:
        input_date = "Дата введена неверно"

    # если дата верна - добавляем значение в таблицу в столбец B
    if input_date != "Дата введена неверно":
        for i in range(1, 1000000):
            if table.sheet1.acell(f'B{i}').value:
                continue
            else:
                table.sheet1.update_acell(f'B{i}', input_date)
                break

    return input_date
