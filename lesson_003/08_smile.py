# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

sd.resolution = (1200, 600)
sd.background_color = (245, 240, 240)

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def smile(point, color):
    # голова смайла
    x = point.x
    y = point.y
    if x < 90:
        x = 90
    elif point.x > 1120:
        x = 1120
    if y < 50:
        y = 50
    elif y > 500:
        y = 500
    # point = sd.get_point(x, y)
    random_delta_x = sd.random_number(50, 100)
    random_delta_y = sd.random_number(40, random_delta_x - 10)
    left_bottom = sd.get_point(x=x - random_delta_x, y=y - random_delta_y)
    right_top = sd.get_point(x=x + random_delta_x, y=y + random_delta_y)
    color = sd.random_color()
    sd.ellipse(left_bottom, right_top, color=color, width=2)

    # глаза
    center_left_eye = sd.get_point(x=x-random_delta_x+sd.random_number(30, 40),
                                   y=y+random_delta_y-sd.random_number(30, 35))
    radius_left_eye = sd.random_number(7, 10)
    # width_left_eye = sd.random_number(2, 4) * sd.random_number(0, 1)
    center_right_eye = sd.get_point(x=x+random_delta_x-sd.random_number(30, 40),
                                   y=y+random_delta_y-sd.random_number(30, 35))
    radius_right_eye = sd.random_number(7, 10)
    # widht_right_eye = sd.random_number(2, 4) * sd.random_number(0, 1)
    sd.circle(center_position=center_left_eye, radius=radius_left_eye, color=color, width=sd.random_number(0,2))
    sd.circle(center_position=center_right_eye, radius=radius_right_eye, color=color, width=sd.random_number(0,2))

    # рот
    point1 = sd.get_point(x=x - random_delta_x + sd.random_number(20, 40),
                          y=y - random_delta_y + sd.random_number(30, 40))
    point2 = sd.get_point(x=x - random_delta_x + sd.random_number(40, 50),
                          y=y - random_delta_y + sd.random_number(15, 25))
    point3 = sd.get_point(x=x + sd.random_number(-10, 10),
                          y=y - random_delta_y + sd.random_number(20, 30))
    point4 = sd.get_point(x=x + random_delta_x - sd.random_number(40, 50),
                          y=y - random_delta_y + sd.random_number(15, 25))
    point5 = sd.get_point(x=x + random_delta_x - sd.random_number(20, 40),
                          y=y - random_delta_y + sd.random_number(30, 45))

    points = [point1, point2, point3, point4, point5]
    random_points_list1 = points[0:sd.random_number(2, 5)]
    random_points_list2 = points[sd.random_number(0, 3):5]
    random_points_list3 = points[::2]
    random_points_list4 = points[1::2]
    random_points_list = sd.choice([random_points_list1, random_points_list2, random_points_list3, random_points_list4])
    closed = sd.choice([True, False])
    sd.lines(point_list=random_points_list, color=color,
             closed=closed, width=sd.random_number(1, 4))


for _ in range(10):
    # smile(X=sd.random_number(70,1140), Y=sd.random_number(50,550), color=None)
    smile(point=sd.random_point(), color=None)

sd.pause()
