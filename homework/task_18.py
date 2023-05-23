# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X
import random

user_length = int(input('enter length: '))

list_nums = []

for i in range(user_length):
    list_nums.append(random.randrange(0, 20))

print(list_nums)

user_num = int(input('enter number: '))
remains = None
result_num = None

for i in list_nums:
    tmp = user_num - i
    if tmp < 0:
        tmp = -tmp
    if remains == None or tmp < remains:
        remains = tmp
        result_num = i

print(result_num)
