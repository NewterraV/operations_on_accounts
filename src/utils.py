import json


def read_json(path):
    """
    Функция получает путь к json-файлу и возвращает данные из него.
    В случае отсутствия данных возвращает "False"
    :param path: Путь к файлу (str)
    :return: Данные (dict, list)
    """
    with open(path, 'r', encoding='utf8') as f:
        dictionary = json.loads(f.read())

    return dictionary


def encrypts_text(item):
    """
    Функция получает строку и возращает её в зашифрованном виде, в случае получения пустой строки возвращает
    так-же пустую строку
    :param item: Строка для шифрования (str)
    :return: Зашифрованная строка (str)
    """

    if not item:
        return ''

    if item[:4].lower() == 'счет':
        return f'{item[:4]} ** {item[-4:]}'

    number = f'{item[-16:-12]} {item[-12:-10]}** **** {item[-4:]}'
    return f'{item[:-17]} {number}'


def format_date(date):
    date_item = date[:10].split('-')
    return f'{date_item[2]}.{date_item[1]}.{date_item[0]}'
