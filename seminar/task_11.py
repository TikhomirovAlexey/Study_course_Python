# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.

user_number = int(input("Ведите целое положительное число: "))
fib_list = [0, 1, 1]
i = 2
if user_number == fib_list[0]: print(1)
elif user_number == fib_list[1] or user_number == fib_list[2]: print('2 and 3')
else:
    while fib_list[i] <= user_number:
        fib_list.append(fib_list[i - 1] + fib_list[i])
        if  fib_list[i + 1] == user_number:
            print(i + 2)
            break
        i += 1
    else: print(-1)
