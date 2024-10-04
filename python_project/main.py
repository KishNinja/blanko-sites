import sys
import math
from random import randint
import turtle
# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.

def randoms():
    a = 120
a = 10
def foo(a = a):
    return a


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