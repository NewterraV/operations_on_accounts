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
        return f'{item[:4]} **{item[-4:]}'

    number = f'{item[-16:-12]} {item[-12:-10]}** **** {item[-4:]}'
    return f'{item[:-17]} {number}'
