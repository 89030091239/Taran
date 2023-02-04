from cat_21_7_1 import Cat

cat1 = Cat('Барон', 'Мальчик', 2)
cat2 = Cat('Сэм', 'Мальчик', 2)

for value in (cat1, cat2):
    print(f'Кличка: {value.getName()}\nПол: {value.getGender()}\nВозраст: {value.getAge()}\n')