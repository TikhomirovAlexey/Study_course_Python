# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.

def get_new_list(size):
    tmp_list = []
    for i in range(size):
        tmp_list.append(int(input(f'введите {i + 1} число: ')))
    return tmp_list

def get_count_num(list_):
    count_tmp = 0
    for i in range(1, len(list_) - 1):
        if list_[i - 1] < list_[i] and list_[i + 1] < list_[i]:
            count_tmp += 1
    return count_tmp


size_user_list = int(input('введите длину масива: '))
user_list = get_new_list(size_user_list)

print(user_list)

count_num = get_count_num(user_list)

print(count_num)
