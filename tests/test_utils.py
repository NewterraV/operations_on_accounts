import pytest
from src.utils import encrypts_text, get_text_operation,get_date

data = {"date": "26.08.2019",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
        "description": "Перевод организации",
        "amount": "31957.58 руб."}

data_2 = {"date": "26.08.2019",
          "from": "",
          "to": "Maestro 1596837868705199",
          "description": "",
          "amount": "31957.58 руб."}

data_3 = {"date": "26.08.2019",
          "from": "Maestro 1596837868705199",
          "to": "",
          "description": "",
          "amount": "31957.58 руб."}


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
