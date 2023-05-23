# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X
import random

user_length = int(input('enter length: '))

list_nums = []

for i in range(user_length):
    list_nums.append(random.randrange(0, 10))

print(list_nums)

user_num = int(input('enter number: '))
count = 0

for i in list_nums:
    if i == user_num:
        count += 1

print(count)
