import pytest
from src.utils import encrypts_text, format_date


@pytest.mark.parametrize('item, result', [('Счет 14211924144426031657', 'Счет ** 1657'),
                                          ("Maestro 1596837868705199", 'Maestro 1596 83** **** 5199'),
                                          ('', '')])
def test_encrypts_text(item, result):
    assert encrypts_text(item) == result


def test_format_date():
    assert format_date('2018-04-14T19:35:28.978265') == '14.04.2018'
