#Task1
print("I like to be a module")

#Файл module.py

#Task1.1
print("I like to be a module")
print(__name__)

#Файл module.py
import module

#Файл main.py

#Task1.2
counter = 0
if __name__ == '__main__':
    print("I prefer to be a module")
else:
    print("I like to be a module")

#Файл module.py

import module
print(module.counter)

#Файл main.py

#Task1.3
__counter = 0
def suml(the_list):
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
        return the_sum
    def prodl(the_list):
        global __counter
        __counter += 1
        prod = 1
        for element in the_list:
            prod *= element
            return prod
if __name__ == '__main__':
    print("I prefer to be a module, but I can do some tests for you.")
    my_list = [i+1 for i in range(5)]
    print(suml(my_list) == 15)

#Файл module.py

from module import suml, prodl

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))

#Файл main.py

#Task1.4
def funA():
    return "Alpha"
if __name__ == "__main__":
    print("I prefer to be a module.")

 # Файл module.py

from sys import path
path.append(r'C:\Users\Admin\PycharmProjects\main\ру\modules')

import module

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))

#Файл main.py

#Task2

from sys import path

path.append("C:\Users\Admin\PycharmProjects\main\ру\packages")

import extra.iota

print(extra.iota.funI())

#Файл main2.py

from sys import path

path.append("C:\Users\Admin\PycharmProjects\main\ру\packages")

import extra.iota import funI
print(funI())

#Task2.1
from sys import path

from ру.packages import extra

path.append("C:\Users\Admin\PycharmProjects\main\ру\packages")

import extra.good.best.sigma as sig
from extra.good.best.tau import funT

print(extra.good.best.sigma.funS())
print(funT())

#Task2.2
from sys import path
path.append("C:\Users\Admin\PycharmProjects\main\ру\packages\Extrapack ZIP file.zip")

import extra.good.best.sigma as sig
import extra.good.alpha as alp
from extra.iota import funT
from extra.good.beta import funB

print(sig.funS())
print(alp.funA())
print(funI())
print(funB())

#Task3

import pygame

run = True
width = 400
height = 100
pygame.init()
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont(None, 48)
text = font.render("Welcome to pygame", True, (255, 255, 255))
screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
pygame.display.flip()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONUP or event.type == pygame.KEYUP:
            run = False
