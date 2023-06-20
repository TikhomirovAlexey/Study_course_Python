# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

def reverse_numbers(size):
    if size == 0:
        return
    num = int(input('enter number: '))
    reverse_numbers(size - 1)
    print(num)


user_size = int(input('enter size: '))

reverse_numbers(user_size)