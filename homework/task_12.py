# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
import random

petya_numbers = []

for i in range(2):
    petya_numbers.append(random.randrange(1, 10))

print(f'sum numbers - {petya_numbers[0] + petya_numbers[1]}, multi - {petya_numbers[0] * petya_numbers[1]}')

while True:
    num_1 = int(input('inter first number: '))
    num_2 = int(input('inter second number: '))
    if num_1 == petya_numbers[0] and num_2 == petya_numbers[1]:
        print('Victory!')
        break
    else: print('False')