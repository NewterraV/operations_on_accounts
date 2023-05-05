from src.utils import encrypts_text, format_date


class Operation:

    def __init__(self, item, ):
        self.id = item["id"]
        self.state = item['state']
        self.date = item['date']
        self.operation_amount = item['operationAmount']
        self.description = item['description'] if 'description' in item.keys() else ''
        self.source = item['from'] if 'from' in item.keys() else ''
        self.to = item['to'] if 'to' in item.keys() else ''

    def __repr__(self):
        return f'id = {self.id}\nstate = {self.state}\ndate = {self.date}\n' \
               f'operation_amount = {self.operation_amount}\ndescription = {self.description}\n' \
               f'from = {self.source}\n to = {self.to}'

    def check_state(self):
        """
        Функция проверяет статус операции. Возвращает True/False
        :return: (bool)
        """
        return self.state.upper() == 'EXECUTED'

    def get_text(self):
        """
        Функция на основе полученого экземпляра класса вовращает сообщение о операции.
        :return: Сообщение (str)
        """

        # Приведение первой строки вывода к необходимому формату
        date = format_date(self.date)
        line = date if not self.description else f'{date} {self.description}'

        # Проверка наличия элементов и на основе их присутствия приведение второй строки к необходимому формату
        if not self.source:
            line_2 = f'-> {encrypts_text(self.to)}'
        elif not self.to:
            line_2 = f'{encrypts_text(self.source)} ->'
        else:
            line_2 = f'{encrypts_text(self.source)} -> {encrypts_text(self.to)}'

        # Приведение третьей строки к необходимому формату
        line_3 = f'{self.operation_amount["amount"]} {self.operation_amount["currency"]["name"]}'

        return f'{line}\n{line_2}\n{line_3}\n'
