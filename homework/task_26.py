# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

def get_result(num: int, deg: int) -> int:
    if deg == 1:
        return num
    return get_result(num, deg - 1) * num

user_number = int(input('enter number: '))
user_degree = int(input('enter degree: '))

print(get_result(user_number, user_degree))
