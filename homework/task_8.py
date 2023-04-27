# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

def get_result(max, count):
    i = 1
    while i <= max:
        if i * max == count:
            return True
        i += 1
    else:
        return False


hight = int(input('введите "высоту" шоколадки: '))
width = int(input('введите "ширину" шоколадки: '))
user_count = int(input('введите количество желаемых долек шоколадки: '))

if hight * width > user_count:
    result = get_result(hight, user_count) or get_result(width, user_count)
    print('yes' if result else 'no')
else:
    print('Неправльное количество долек')
