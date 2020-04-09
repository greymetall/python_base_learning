# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

sd.resolution = (1200, 600)


# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

def brick(x, y, height, width, color):
    start_point = sd.get_point(x, y)
    x1 = x + width
    y1 = y + height
    end_point = sd.get_point(x1, y1)
    sd.rectangle(left_bottom=start_point, right_top=end_point, color=color, width=width_line)

x, y = -50, 0
for y in range(0, 750, 50):
    if not y % 100:
        for x in range(-50, 1250, 100):
            if x % 150:
                width_line = 2
            else:
                width_line = 0
            brick(x=x, y=y, height=50, width=100, color=sd.COLOR_DARK_ORANGE)
            # else:
            #     brick(x=x, y=y, height=50, width=100, color=sd.COLOR_DARK_ORANGE)
    else:
        for x in range(0, 1200, 100):
            if x % 150:
                width_line = 0
            else:
                width_line = 2
            brick(x=x, y=y, height=50, width=100, color=sd.COLOR_DARK_ORANGE)

# brick(x=50, y=50, height=50, width=100, color=sd.COLOR_DARK_ORANGE)


sd.pause()