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


def get_text_operation(item):
    """
    Функция принимает словарь созданный функцией класса Operation
    и на основе него создает орматированный текст для вывода.
    :param item: Словарь на основе Operation.get_dict (dict)
    :return: Текст (str)
    """

    line = item['date'] if not item['description'] else f'{item["date"]} {item["description"]}'

    if not item['from']:
        line_2 = f'-> {encrypts_text(item["to"])}'

    elif not item['to']:
        line_2 = f'{encrypts_text(item["from"])} ->'

    else:
        line_2 = f'{encrypts_text(item["from"])} -> {encrypts_text(item["to"])}'

    return f'{line}\n{line_2}\n{item["amount"]}\n'
