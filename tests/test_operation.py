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
    "from": "Счет 27248529432547658655",
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
}


@pytest.mark.parametrize('item, result', [(data,
                                           {"date": "26.08.2019",
                                            "from": "Maestro 1596837868705199",
                                            "to": "Счет 64686473678894779589",
                                            "description": "Перевод организации",
                                            "amount": "31957.58 руб."}),
                                          (data_2, {}),
                                          (data_3, {"date": "26.08.2019",
                                                    "from": "",
                                                    "to": "",
                                                    "description": "",
                                                    "amount": "31957.58 руб."})])
def test_get_dict(item, result):
    instance = Operation(item)
    assert instance.get_dict() == result
