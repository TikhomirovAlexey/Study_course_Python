# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0
#  = 0, a1
#  = 1, ak
#  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 13
# Задание необходимо решать через рекурсию

def fib(num):
    if num in (0, 1):
        return 1
    return fib(num - 1) + fib(num - 2)

user_number = int(input('enter the number: '))

result = fib(user_number)
print(result)