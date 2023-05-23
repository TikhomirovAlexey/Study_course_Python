# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

list_numbers = [1, 2, 3, 4, 5]
# output_list = []

step = int(input('inter step: '))

# if step > len(list_numbers) or step < 1:
#     print('error')
# else:
#     for i in range(len(list_numbers)):
#         output_list.append(list_numbers[-step + 1 + i])
#     print(list_numbers)
#     print(output_list)

if step > len(list_numbers) or step < 1:
    print('error')
else:
    for i in range(step - 1):
        list_numbers.insert(0, list_numbers.pop())
    print(list_numbers)








