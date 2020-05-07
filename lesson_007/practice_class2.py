from random import randint
from termcolor import cprint


# Создадим двух людей, живущих в одном доме - Бивиса и Батхеда
# Нужен класс Дом, в нем должн быть холодильник с едой и тумбочка с деньгами
# Еда пусть хранится в холодильнике в доме, а деньги - в тумбочке.

# Создаем класс для людей
class Man:
    """ Атрибуты класса (описание объекта)"""

    def __init__(self, name):  # Объявление метода через конструктор
        self.name = name  # Имя
        self.fullness = 50  # Сытость
        self.house = None  # Описание дома

    """ Методы класса (действия объекта)"""

    def __str__(self):  # Объект рассказывает о своем состоянии
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):  # Ест
        if self.house.food >= 10:  # Если в доме еды больше или 10, то
            cprint('{} поел'.format(self.name), color='yellow')  # Объект поел
            self.fullness += 10  # сытости добавилось
            self.house.food -= 10  # еды убавилось
        else:  # Иначе
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):  # Работает
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 50
        self.fullness -= 10

    def watch_MTV(self):  # Смотрит телевизор
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):  # Ходит в магазин
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def go_to_the_house(self, house):  # Заселяется в дом
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def act(self):  # Действия объекта
        if self.fullness <= 0:  # Если сытость <= 0, то
            cprint('{} умер...'.format(self.name), color='red')
            return  # вернуть
        dice = randint(1, 6)  # значение кубика
        if self.fullness < 20:  # если сытость меньше 20, то
            self.eat()  # ест
        elif self.house.food < 10:  # если еды меньше 10, то
            self.shopping()  # идет в магазин
        elif self.house.money < 50:  # иначе если денег меньше 10, то
            self.work()  # идет на работу
        elif dice == 1:  # иначе если на кубике 1, то
            self.work()  # работает
        elif dice == 2:  # иначе если 2, то
            self.eat()  # ест
        else:  # иначе
            self.watch_MTV()  # смотрит телевизор

# Создаем класс для домов
class House:

    def __init__(self):
        self.food = 50
        self.money = 0

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}'.format(
            self.food, self.money)

# Если однотипных объектов много, их проще перечислить в списке
citizens = [
    Man(name='Бивис'),
    Man(name='Батхед'),
    Man(name='Кенни'),
]
# Затем, для каждого объекта из списка задавать действия (методы)
my_sweet_home = House()
for citisen in citizens:
    citisen.go_to_the_house(house=my_sweet_home)

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    for citisen in citizens:
        citisen.act()
    print('--- в конце дня ---')
    for citisen in citizens:
        print(citisen)
    print(my_sweet_home)

""" План претерпел изменения:
    1. Надо понять, какие у нас будут объекты
    1. Для каждого однотипного объекта создаем класс
    2. Создаем объекты, которым присваиваем имя этого класса
    3. Описываем свойства (аргументы) объектов
    4. Описываем действия (методы) объектов
    5. Вызываем объекты и заставляем их (по необходимости) действовать через методы, прописанные ранее
    Прим. Для раскрашивания устанавливаем в пайчарм пакет termcolor"""
