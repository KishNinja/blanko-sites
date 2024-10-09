import sys
import os
import math
from random import randint
import turtle
import datetime
import json
import requests

time = datetime.datetime.now()

___ = datetime.datetime.now()

with open('python_project/date.json', 'r', encoding='utf-8') as file:
    oxxxymiron_json = json.load(file)

class Phone:
    def __init__(self, name, color, price, orm, memory) -> None:
        self.name = name
        self.color = color
        self.price = price
        self.orm = orm
        self.memory = memory
    # В метод __str__ не записуется аргументы кроме self.
    def __str__(self):
        return f'Name phone - {self.name}\nColor phone - {self.color}\nPrice phone - {self.price}\nCount orm - {self.price}\nCount memory - {self.price}'
    
    def __norma_phone__(self):
        total = self.memory / self.orm
        if total > 10:
            return 'Norma'
        return 'No norma, It phone old'

class Iphone(Phone):
    def __init__(self, name, color, price, orm, memory, ios):
        super().__init__(name, color, price, orm, memory)
        self.ios = ios
    def __str__(self):
        # super это обращение к предыдущему куску кода который находится в 
        # классе родитель.
        return f'{super().__str__()}\nIOS - {self.ios}'

class Enemy():
    def __init__(self, name, hp) -> None:
        self.name = name
        self.hp = hp 

class Guns():
    def __init__(self, damage) -> None:
        self.damege = damage

    # Когда мы передаем в метод объект, то нам предаставляются вся информация объекта.
    def __damage_fnc__(self, emeny) -> None:
        i = 0
        while emeny.hp > 0:
            emeny.hp -= self.damege  
            i += 1
            if emeny.hp == 0:
                break
        return f'Было нанесено {i} удара, {emeny.name} убит.'