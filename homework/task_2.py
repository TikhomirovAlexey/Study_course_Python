# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

user_number = int(input('Введите трехзначное число: '))

result = user_number // 100 + (user_number // 10 % 10) + user_number % 10

print(result)
