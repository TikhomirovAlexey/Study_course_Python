# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

def write_phonebook(path, new_list_subscribers):
    str_phonebook = "".join(new_list_subscribers) 
    with open(path, 'w', encoding='UTF-8') as write_file:
        write_file.write(str_phonebook)

def print_phonebook(path):
    with open(path, 'r', encoding='UTF-8') as read_file:
        for line in read_file:
            print(line)

def search_phonebook(path, search_option):
    have = False
    with open(path, 'r', encoding='UTF-8') as read_file:
        list_subscribers = read_file.readlines()
        for item in range(len(list_subscribers)):
            if search_option in list_subscribers[item].lower():
                have = True
                return [list_subscribers[item], item]

    if not have: print('Такого абонента нет!')

def append_phonebook(path, phone, name):
    with open(path, 'a', encoding='UTF-8') as append_file:
        append_file.write(f'{name} - {phone}\n')
        print(f'Новая запись: {name} - {phone}.')

def change_subscriber(path, list_subs_ind):
    with open(path, 'r', encoding='UTF-8') as read_file:
        list_subscribers = read_file.readlines()
        cange_option = int(input('Введите опцию: 1 - изменить ФИО; 2 - изменить номер. '))
        list_subs = list_subscribers[list_subs_ind[1]].strip().split('-')
        if cange_option == 1:
            list_subs[0] = input('Введите новое значение ФИО: ')
        elif cange_option == 2:
            list_subs[1] = input('Введите новое значение номера: ')
        else: print('Неправильная команда!')
        list_subscribers[list_subs_ind[1]] = f'{list_subs[0]} - {list_subs[1]}\n'
        print(f'Отредактировано: {list_subs[0]} - {list_subs[1]}.')

        return list_subscribers
    
def delete_subscriber(path, list_subs_ind):
    with open(path, 'r', encoding='UTF-8') as read_file:
        list_subscribers = read_file.readlines()
        yes_or_no = int(input(f'Удалить {list_subs_ind[0]}? Введите 1 - да, 2 - нет! '))
        if yes_or_no == 1:
            del list_subscribers[list_subs_ind[1]]
            print(f'Удалено {list_subs_ind[0]}')
        elif yes_or_no == 2:
            print('Отменено!')
        else: print('Неправильная команда!')
        return list_subscribers


path_phonebook = 'phonebook.txt'

user_option = int(input('Введите команду: \n1 - Вывести весь телефонный справочник; 2 - Поиск нужного абонента; 3 - Запись нового абонента; 4 - Редактировать запись; 5 - Удалить запись. '))

if user_option == 1:
    print_phonebook(path_phonebook)
elif user_option == 2 or user_option == 4 or user_option == 5:
    user_search = input('Введите ФИО или номер абонента: ').lower()
    list_name_idex_subscriber = search_phonebook(path_phonebook, user_search)
    print(list_name_idex_subscriber[0])
    if user_option == 4:
        new_list_phonebook = change_subscriber(path_phonebook, list_name_idex_subscriber)
        write_phonebook(path_phonebook, new_list_phonebook)
    if user_option == 5:
        new_list_phonebook = delete_subscriber(path_phonebook, list_name_idex_subscriber)
        write_phonebook(path_phonebook, new_list_phonebook)        
elif user_option == 3:
    append_phone = input('Введите номер: ')
    append_name = input('Введите ФИО: ')
    append_phonebook(path_phonebook, append_phone, append_name)
else: print('Неправильная команда!')



