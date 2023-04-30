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

    def get_dict(self):
        """
        Функция на основе полученого экземпляра класса вовращает словарь для вывода операции
        при условии что статус операции "Выполнена". В противном случае возвращает пустой словарь
        :return:(dict)
        """
        if self.state.lower() == 'canceled':
            return {}

        date = self.date[:10].split('-')

        return {"date": f'{date[2]}.{date[1]}.{date[0]}',
                "from": self.source,
                "to": self.to,
                "description": self.description,
                "amount": f'{self.operation_amount["amount"]} {self.operation_amount["currency"]["name"]}'}
