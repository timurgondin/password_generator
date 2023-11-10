import random


def error():  # функция для вывода сообщения об ошибке красным цветом
    print('\033[31m{}'.format('Ошибка'))


print(
    'Добро пожаловать в генератор паролей!')
print()

lowercase = 'abcdefghijklmnopqrstuvwxyz'  # набор букв нижнего регистра
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # набор букв верхнего регистра
digits = '0123456789'  # набор цифр от 0 до 9
symbols = '!";#$%&()*+,-./:;<=>?@[]^_`{|}~'  # набор специальных символов

pwd = []  # список с элементами, которые будут в пароле

length = int(input('Укажите длину пароля: '))
print()

what_case_letters = int(input('Буквы какого регистра использовать?\n1 - Нижнего\n2 - Верхнего\n3 - Разного\nВыбор: '))
print()

if what_case_letters != 1 and what_case_letters != 2 and what_case_letters != 3:
    error()  # вывод сообщения об ошибке, если пользователь выбрал не то
else:
    if what_case_letters == 1:
        pwd.extend(lowercase)  # добавляет в список буквы нижнего регистра
    elif what_case_letters == 2:
        pwd.extend(uppercase)  # добавляет в список буквы верхнего регистра
    elif what_case_letters == 3:
        pwd.extend(lowercase)  # добавляет в список буквы нижнего регистра
        pwd.extend(uppercase)  # добавляет в список буквы верхнего регистра

    if_digits = int(input('Использовать цифры?\n1 - Да\n2 - Нет\nВыбор: '))
    print()

    if (if_digits != 1) and (if_digits != 2):
        error()  # вывод сообщения об ошибке, если пользователь выбрал не то
    else:
        if if_digits == 1:
            pwd.extend(digits)  # добавляет в список цифры

        if_symbols = int(input('Использовать специальные символы?\n1 - Да\n2 - Нет\nВыбор: '))
        print()

        if if_symbols != 1 and if_symbols != 2:
            error()  # вывод сообщения об ошибке, если пользователь выбрал не то
        else:
            if if_symbols == 1:
                pwd.extend(symbols)  # добавляет в список специальные символы

            quantity = int(input('Сколько паролей сгенерировать? '))
            print()

            for i in range(quantity):  # цикл для вывода нескольких паролей
                for k in range(length):  # цикл для управления количеством символов в пароле
                    print(random.choice(pwd), end='')
                print()