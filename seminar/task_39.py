# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
import random

def get_new_list(size):
    tmp_list = []
    for i in range(size):
        tmp_list.append(random.randrange(0, 20))
    return tmp_list

def unique_num(list_1, list_2):
    tmp_list = []
    for i in list_1:
        if i in list_2:
           tmp_list.append(i)
    return tmp_list

size_first_list = int(input('введите длину первого масива: '))
first_list = get_new_list(size_first_list)
size_second_list = int(input('введите длину второго масива: '))
second_list = get_new_list(size_second_list)
print(first_list)
print(second_list)

result_list = unique_num(first_list, second_list)
print(result_list)
