# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations_.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.


class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


def tester_files(line):
    # print(f'Read line {line}', flush=True)
    length = len(line.split())
    if length < 3:
        raise ValueError(f'Недостаточно данных. Обнаружено: {length} требуетя: 3')
    elif length > 3:
        raise ValueError(f'Данных больше, чем нужно. Обнаружено: {length} требуетя: 3')
    else:
        name, email, age = line.split(' ')
    if not name.isalpha():
        raise NotNameError('Имя содержит недопустимые символы')
    if '@' not in email and '.' not in email:
        raise NotEmailError('Несуществующий email')
    if age.isnumeric():
        if not 10 <= int(age) <= 99:
            raise ValueError('Возраст вне диапазона от 10 до 99')
    else:
        raise ValueError('Возраст не распознан')


good_log = open('registrations_good.log', 'w', encoding='utf8')
bad_log = open('registrations_bad.log', 'w', encoding='utf8')
with open('registrations.txt', 'r', encoding='utf8') as ff:
    for number, string in enumerate(ff, 1):
        number, string = str(number) + '.', string[:-1]
        output = number + string + ' - error: '
        try:
            tester_files(line=string)
        except ValueError as exc:
            bad_log.write(output + exc.args[0] + '\n')
            print(output + exc.args[0])
        except NotNameError as exc:
            bad_log.write(output + exc.args[0] + '\n')
            print(output + exc.args[0])
        except NotEmailError as exc:
            bad_log.write(output + exc.args[0] + '\n')
            print(output + exc.args[0])
        except Exception as exc:
            bad_log.write(output + exc.args[0] + '\n')
            print(output + 'Неизвестная ошибка:', exc.args[0])
        else:
            good_log.write(number + string + '\n')
good_log.close()
bad_log.close()


# import os
# os.chdir(r'D:\Курсы\Skillbox\Основы_Python\python_homeworks\lesson_010')
# print(os.getcwd())
# print(os.listdir(os.getcwd()))
# print(os.path.abspath('registrations_.txt'))
# print(os.path.abspath('registrations_.txt'))
# print(os.getcwd())
# os.defpath(registrations_.txt)
