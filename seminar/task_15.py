# Задача №15. Решение в группах
# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

count_watermelons = int(input('Count watermelons: '))

min_weigh = 0
max_weigh = 0

for i in range(count_watermelons):

    tmp_weigh = int(input('Weigh watermelons: '))
    
    if min_weigh == 0 and max_weigh == 0:
        min_weigh = min_weigh = tmp_weigh
    else: 
        if tmp_weigh > max_weigh:
            max_weigh = tmp_weigh
        if tmp_weigh < min_weigh:
            min_weigh = tmp_weigh

print(f'min - {min_weigh}, max - {max_weigh}')