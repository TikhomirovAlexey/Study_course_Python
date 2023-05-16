# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120

user_number = int(input('Введите целое неотрицательное число: '))
count = 1
multi = 1
while count <= user_number:
    multi *= count
    count += 1
print(multi)
