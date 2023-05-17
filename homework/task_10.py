# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

count_coins = int(input('inter count coints: '))

count_front = 0
count_back = 0

for i in range(count_coins):
    tmp_num = int(input(f'inter side {i + 1} (1 - front or 0 - back): '))
    if tmp_num:
        count_front += 1
    else: count_back += 1

print(count_front if count_front < count_back else count_back)
