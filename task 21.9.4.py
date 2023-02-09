class Client:
    def __init__(self, name, surname, city):
        self.name = name
        self.surname = surname
        self.city = city

    def information(self):
        return f"{self.name} {self.surname} {self.city}"


clients = [
    {
        "name": "Иван",
        "surname": "Иванов",
        "city": "Москва",
        "wallet_balance": 1000,
    },
    {
        "name": "Петр",
        "surname": "Петров",
        "city": "Казань",
        "wallet_balance": 950,
    },
    {
        "name": "Нгуен",
        "surname": "Нгуен",
        "city": "Хошимин",
        "wallet_balance": 10000,
    },
]
lst = []
for client in clients:
    customer_data = Client(name=client.get("name"),
                           surname=client.get("surname"),
                           city=client.get("city"))
    lst.append(customer_data.information().split())
print(lst)
