# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий

bushes_count = int(input('введите количество кустов: '))

list_count_berries = []

for i in range(bushes_count):
    list_count_berries.append(int(input(f'введите количество ягод на {i + 1} кусте: ')))

max_count_berries = -1
for i in range(len(list_count_berries)):
    tmp_num = 0
    if i == 0:
        tmp_num = list_count_berries[-1] + list_count_berries[0] + list_count_berries[1]
    elif i == len(list_count_berries) - 1:
        tmp_num = list_count_berries[len(list_count_berries) - 2] + list_count_berries[len(list_count_berries) - 1] + list_count_berries[0]
    else:
        tmp_num = list_count_berries[i - 1] + list_count_berries[i] + list_count_berries[i + 1]
    if max_count_berries < tmp_num:
        max_count_berries = tmp_num

print(max_count_berries)
