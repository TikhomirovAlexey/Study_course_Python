# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.

user_num = int(input('inter number: '))

list_numbers = []

for i in range(user_num):
    tmp_num = 2 ** i
    if tmp_num <= user_num:
        list_numbers.append(tmp_num)
    else: break

print(list_numbers)
