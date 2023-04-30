import pytest
from src.utils import encrypts_text


@pytest.mark.parametrize('item, result', [('Счет 14211924144426031657', 'Счет **1657'),
                                          ("Maestro 1596837868705199", 'Maestro 1596 83** **** 5199'),
                                          ('', '')])
def test_encrypts_text(item, result):
    assert encrypts_text(item) == result
