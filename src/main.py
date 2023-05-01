from src.cnst import PATH_OPERATIONS
from src.utils import read_json
from src.classes.operation import Operation


def main(path):
    list_operations = list(reversed(read_json(path)))
    list_text = []

    for i in list_operations:
        if len(list_text) == 5:
            break
        instance = Operation(i)

        if not instance.check_state():
            continue
        list_text.append(instance.get_text())

    for i in list_text:
        print(i)

    return True


main(PATH_OPERATIONS)
