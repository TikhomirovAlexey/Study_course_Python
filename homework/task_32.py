# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
import random

def get_generate_list():
    tmp_list = []
    for i in range(20):
        tmp_list.append(random.randrange(-20, 20))
    return tmp_list

def get_list_index_range(list_p, min_r, max_r):
    tmp_list = []
    for i in range(len(list_p)):
        if min_r <= list_p[i] <= max_r:
            tmp_list.append(i)
    return tmp_list


min_user_range = int(input('enter minimum range: '))
max_user_range = int(input('enter maximum range: '))

generate_list = get_generate_list()
print(generate_list)

list_index_range = get_list_index_range(generate_list, min_user_range, max_user_range)
print(list_index_range)