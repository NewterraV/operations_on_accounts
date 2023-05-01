import pytest
from src.classes.operation import Operation

data = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
        "amount": "31957.58",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
}

data_2 = {
    "id": 649467725,
    "state": "CANCELED",
    "date": "2018-04-14T19:35:28.978265",
    "operationAmount": {
        "amount": "96995.73",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    },
    "description": "Перевод организации",
    "from": "",
    "to": "Счет 97584898735659638967"
}

data_3 = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
        "amount": "31957.58",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    },
    "to": "Счет 97584898735659638967"
}

data_4 = {
    "id": 649467725,
    "state": "EXECUTED",
    "date": "2018-04-14T19:35:28.978265",
    "operationAmount": {
        "amount": "96995.73",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    },
    "description": "",
    "from": "Счет 97584898735659638967",
    "to": ""
}


@pytest.mark.parametrize('item, result', [
    (data, f'26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет ** 9589\n31957.58 руб.\n'),
    (data_3, f'26.08.2019\n-> Счет ** 8967\n31957.58 руб.\n'),
    (data_4, f'14.04.2018\nСчет ** 8967 ->\n96995.73 руб.\n')])
def test_get_text(item, result):
    assert Operation(item).get_text() == result


@pytest.mark.parametrize('item, result', [(data, True), (data_2, False)])
def test_check_state(item, result):
    assert Operation(item).check_state() == result
