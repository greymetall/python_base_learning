from random import randint


# Реализуем модель человека
# Человек может есть, работать, играть, ходить в магазин
# У человека есть степень сытости, немного еды и денег
# Если сытость < 0 единиц, человек умирает
# Человеку надо прожить 365 дней
from termcolor import cprint


class Man:
    """ Атрибуты класса (описание объекта)"""
    def __init__(self, name):   # Объявление метода через конструктор
        self.name = name        # Имя
        self.fullness = 50       # Сытость
        self.food = 50          # Сколько есть еды
        self.money = 0          # Сколько есть денег

    """ Методы класса (действия объекта)"""
    def __str__(self):          # Объект рассказывает о себе:
        return 'Я - {}, сытость - {}, еды осталось - {}, денег осталось - {}'.format(
            self.name, self.fullness, self.food, self.money)

    def eat(self):                                      # Объект ест
        if self.food >= 10:                             # Если еды больше 10, тогда
            print('{} поел'.format(self.name))          # вывести "Вася поел",
            self.fullness += 10                         # к сытости добавить 10,
            self.food -= 10                             # от еды убавить 10
        else:   # Иначе:
            print('{} без еды'.format(self.name))       # вывести "Вася без еды",

    def work(self):             # Объект работает
        cprint('{} сходил на работу'.format(self.name), color='magenta')  # Вывести "Вася сходил на работу"
        self.money += 50                                # к деньгам добавить 50
        self.fullness -= 10                             # от сытости отнять 10

    def play_dota(self):
        cprint('{} играл в доту целый день'.format(self.name), color='green')  # Вывести "Вася играл в доту целый день"
        self.fullness -= 10  # от сытости отнять 10

    def shopping(self):
        if self.money >= 50:
            print('{} пошел в магазин'.format(self.name))  # Вывести "Вася пошел в магазин"
            self.food += 50
            self.money -= 50
        else:
            print('{} деньги кончились'.format(self.name))  # Вывести "Вася деньги кончились"

    def act(self):
        if self.fullness <= 0:                          # Если сытость <= 0
            print('{} умер'.format(self.name))          # вывести "Вася умер"
            return                                      # вернуть
        dice = randint(1, 6)                            # значение кубика
        if self.fullness < 20:                          # если сытость меньше 20, то
            self.eat()                                  # ест
        elif self.food < 10:                            # если еды меньше 10, то
            self.shopping()                             # идет в магазин
        elif self.money < 10:                           # иначе если денег меньше 10, то
            self.work()                                 # идет на работу
        elif dice == 1:                                 # иначе если на кубике 1, то
            self.work()                                 # работает
        elif dice == 2:                                 # иначе если 2, то
            self.eat()                                  # ест
        else:                                           # иначе
            self.play_dota()                            # играет


vasya = Man(name='Вася')      # Создали объект класса Man с именем Вася

for day in range(1, 21):      # Для любого из дней в диапозоне от 1 до 21
    cprint('========= день {} ========='.format(day), color='yellow')    # вывести день (любое число),
    vasya.act()                                         # действия Васи
    print(vasya)

""" План такой:
    1. Создаем класс
    2. Создаем объект, которому присваиваем имя этого класса
    3. Описываем свойства (аргументы) объекта
    4. Описываем действия (методы) объекта
    5. Вызываем объект и заставляем его (по необходимости) действовать через методы, прописанные ранее
    Прим. Для раскрашивания устанавливаем в пайчарм пакет termcolor"""
