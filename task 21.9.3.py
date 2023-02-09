class Client:
    def __init__(self, name, surname, city, wallet_balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.wallet_balance = wallet_balance

    def information(self):
        return f"«{self.name} {self.surname}. {self.city}. Баланс: {self.wallet_balance} руб.»"


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

for client in clients:
    customer_data = Client(name=client.get("name"),
                           surname=client.get("surname"),
                           city=client.get("city"),
                           wallet_balance=client.get(
                               "wallet_balance"))  # Здесь мы использовали метод словаря .get(),
    # Который не вызовет ошибку, если такого ключа в словаре нет.
    print(customer_data.information())
