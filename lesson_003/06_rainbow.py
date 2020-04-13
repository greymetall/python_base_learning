# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd
sd.resolution = (1200, 600)
sd.background_color = (138, 172, 255)

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# step = 0
# for color in rainbow_colors:
#     start_point = sd.get_point(50, 300-step)
#     end_point = sd.get_point(850, 650-step)
#     step += 30
#     sd.line(start_point=start_point, end_point=end_point, color=color, width = 30)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

step = 0
for color in rainbow_colors[::-1]:
    center = sd.get_point(715, -500)
    sd.circle(center_position=center, radius=1050-step, color=color, width=30)
    step += 30
sd.pause()
