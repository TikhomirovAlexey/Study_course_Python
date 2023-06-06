# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества.
import random

def get_random_set(size):
    tmp_set = set()
    for i in range(size):
        tmp_set.add(random.randrange(0, 20))
    return tmp_set

size_one = int(input('введите размер первого множества: '))
size_two = int(input('введите размер второго множества: '))

set_one = get_random_set(size_one)
set_two = get_random_set(size_two)

list_result = list(set_one.intersection(set_two))

if list_result == []:
    print('нет одинаковых значений')
else:
    list_result.sort()
    print(set_one)
    print(set_two)
    print(list_result)

