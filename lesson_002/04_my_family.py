#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = []
my_family.extend(['я', 'мама', 'сестра', 'дед', 'отец'])
print(my_family)

# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    [],
]
my_family_height *= 5
my_family_height[0] = ([my_family[0], 186])
my_family_height[1] = ([my_family[1], 175])
my_family_height[2] = ([my_family[2], 170])
my_family_height[3] = ([my_family[3], 168])
my_family_height[4] = ([my_family[4], 175])
print(my_family_height)

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print('Рост отца -', my_family_height[4][1], 'см')
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
sum_heights = my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1] + my_family_height[3][1] + \
              my_family_height[4][1]
sum_test = 0
# for i in my_family_height:
# sum_test += i[1]
print('Общий рост моей семьи:', sum_heights, )  # sum_test
