# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def get_generate_list(start, step, count):
    while count > 0:
        print(start)
        start += step
        count -= 1


start_number = int(input('enter start-number: '))
step_number = int(input('enter step-number: '))
count_number = int(input('enter count-number: '))

result_list = get_generate_list(start_number, step_number, count_number)

