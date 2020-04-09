#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь магазинов с распродажами
from pprint import pprint
shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
}

# Создайте словарь цен на продукты следующего вида (писать прямо в коде)
sweets = {
    'название сладости': [
        {'shop': 'название магазина', 'price': 99.99},
        # тут с клавиатуры введите магазины и цены (можно копипастить ;)
    ],
    # тут с клавиатуры введите другую сладость и далее словарь магазинов
}
# Указать надо только по 2 магазина с минимальными ценами

auchan = list(shops.keys())[0]
pyatyorka = list(shops.keys())[1]
magnit = list(shops.keys())[2]

sweets = {
    shops['ашан'][0]['name']: [
        {'shop': auchan, list(shops['ашан'][0].keys())[1]: shops['ашан'][0]['price']},
        {'shop': pyatyorka, list(shops['пятерочка'][0].keys())[1]: shops['пятерочка'][0]['price']}
        ],
    shops['ашан'][1]['name']: [
        {'shop': pyatyorka, list(shops['пятерочка'][1].keys())[1]: shops['пятерочка'][1]['price']},
        {'shop': magnit, list(shops['магнит'][1].keys())[1]: shops['магнит'][1]['price']},
        ],
    shops['ашан'][2]['name']: [
        {'shop': auchan, list(shops['ашан'][2].keys())[1]: shops['ашан'][2]['price']},
        {'shop': magnit, list(shops['магнит'][2].keys())[1]: shops['магнит'][2]['price']},
        ],
    shops['ашан'][3]['name']: [
        {'shop': pyatyorka, list(shops['пятерочка'][3].keys())[1]: shops['пятерочка'][3]['price']},
        {'shop': magnit, list(shops['магнит'][3].keys())[1]: shops['магнит'][3]['price']},
        ],
}
pprint(sweets)