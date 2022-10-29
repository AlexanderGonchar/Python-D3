# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] => на нечётных позициях элементы 3 и 9, ответ: 12

import random

n = int(input('Сколько чисел будет в списке? : '))
a = int(input('Введите чило a : '))
b = int(input('Введите число b : '))

numberslist = []

for i in range(n):
     numberslist.append(random.randint(a, b))

print(numberslist)

sumnumbers = 0

for i in range(1, n, 2):
    sumnumbers += numberslist[i]

print(sumnumbers)
