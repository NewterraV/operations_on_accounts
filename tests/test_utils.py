import pytest
from src.utils import encrypts_text, get_text ,get_date


@pytest.mark.parametrize('item, result', [('Счет 14211924144426031657', 'Счет ** 1657'),
                                          ("Maestro 1596837868705199", 'Maestro 1596 83** **** 5199'),
                                          ('', '')])
def test_encrypts_text(item, result):
    assert encrypts_text(item) == result


@pytest.mark.parametrize('item, result', [
    (data, f'26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет ** 9589\n31957.58 руб.\n'),
    (data_2, f'26.08.2019\n-> Maestro 1596 83** **** 5199\n31957.58 руб.\n'),
    (data_3, f'26.08.2019\nMaestro 1596 83** **** 5199 ->\n31957.58 руб.\n')
])
def test_get_text_operation(item, result):
    assert get_text_operation(item) == result


def test_get_date():
    assert get_date({'id': '1324', 'date': '24.06.2019'}) == '24.06.2019'


def test_format_date():
    assert format_date('2018-04-14T19:35:28.978265') == '14.04.2018'
