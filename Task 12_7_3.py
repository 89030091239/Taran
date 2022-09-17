
# ЗАДАНИЕ 12.7.3 (HW-03)

money_sum = float(input("Введите сумму:"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = money_sum/100

max_val = max(per_cent.values())
story_count = {k:v for k, v in per_cent.items() if v == max_val}

name = story_count.keys()
for name_bank in name:

 procent = story_count.values()
 for elem in procent:

  deposit = elem*money

print("Название банка: ", name_bank,", Максимальная сумма, которую вы можете заработать: ", deposit, sep="")
