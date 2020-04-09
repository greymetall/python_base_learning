# -*- coding: utf-8 -*-

# (цикл while)

# даны целые положительные числа a и b (a > b)
# Определить результат целочисленного деления a на b, с помощью цикла while,
# __НЕ__ используя стандартную операцию целочисленного деления (// и %)
# Формат вывода:
#   Целочисленное деление ХХХ на YYY дает ZZZ

a, b = 0, 1
c = 0
difference = a
if a < 0 or b < 0:
    print('Error. Out of range!')
elif (type(a) is float) or (type(b) is float):
    print('Error. Parameters a and b must be integers')
elif b >= 1:
    while difference >= b:
        difference -= b
        c += 1
    print('Целочисленное деление {} на {} дает {}'.format(a, b, c))
else:
    print("На ноль делить нельзя!")
c = a // b
print('Проверка. Правильный ответ:', c)
