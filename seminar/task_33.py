# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

def get_grades_list(count):
    list_gr = []
    for i in range(count):
        list_gr.append(int(input(f'Ведите {i + 1} оценку: ')))
    return list_gr

def replacing_grades(gr_list, min, max, copy = True):
    if copy:
        gr_list = gr_list.copy()
    while max in gr_list:
        gr_list[gr_list.index(max)] = min
    return gr_list
    

grades_list = get_grades_list(int(input('Введите количество оценок: ')))

print(grades_list)

min_value = min(grades_list)
max_value = max(grades_list)

print(replacing_grades(grades_list, min_value, max_value))