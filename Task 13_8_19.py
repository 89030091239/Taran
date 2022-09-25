#   ЗАДАНИЕ 13.8.19 (HW-03)

tickets = int(input("Укажите количество билетов, которое хотите приобрести:"))
age = [int(input("Введите возраст посетителя для каждого билета:")) for i in range(tickets)]  # Генератор спискa

price_age = []  # Создаем пустой список
for i in age:
    if i in range(0, 18):  #  range(старт, стоп, шаг) диапазон выбора
        price_age.append(0)
    elif i in range(18, 25):
        price_age.append(990)  #  .append() добавляет элемент в конец списка
    else:
        price_age.append(1390)

if tickets > 3:
    discount = sum(price_age) - ((sum(price_age) / 100) * 10)
    print(f"Сумма к оплате {discount} руб. с учетом скидки 10%")
else:
    price = sum(price_age)
    print(f"Сумма к оплате {price} руб.")
