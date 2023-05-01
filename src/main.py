import json

from src.cnst import PATH_OPERATIONS
from src.utils import read_json, get_text_operation, get_date
from src.classes.operation import Operation


def main(path):
    list_json = read_json(path)
    list_json.remove({})
    list_operations = sorted(list_json, key=get_date, reverse=True)
    list_text = []

    for i in list_operations:
        if len(list_text) == 5:
            break
        instance = Operation(i)
        dict_instance = instance.get_dict()

        if not dict_instance:
            continue
        list_text.append(get_text_operation(dict_instance))

    for i in list_text:
        print(i)

    return True


main(PATH_OPERATIONS)
