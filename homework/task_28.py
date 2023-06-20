# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

def get_sum_numbers(num_1: int, num_2: int) -> int:
    if num_2 == 0:
        return num_1
    return get_sum_numbers(num_1, num_2 - 1) + 1

number_1 = int(input('enter number_1: '))
number_2 = int(input('enter number_2: '))

print(get_sum_numbers(number_1, number_2))
