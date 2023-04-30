from src.cnst import PATH_OPERATIONS
from src.main import main


def test_main():
    assert main(PATH_OPERATIONS) is True
