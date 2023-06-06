# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

letters_list = input('введите буквы через пробел: ').split()

count_dict = {}

list_result = ''

for i in letters_list:
    if list_result == '':
        list_result += f'{i}'
    else:
        list_result += f' {i}'
        if i in count_dict:
            list_result += f'_{count_dict[i]}'
            count_dict[i] += 1
        else:
            count_dict[i] = 1

print(list_result)