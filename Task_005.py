""" Реализуйте алгоритм перемешивания списка. """

from random import shuffle
import random

print('Вариант 1')
list = [1, 2, 3, 4, 5]
print(list)
shuffle(list)
print(list)

print('Вариант 2')
list = [1, 2, 3, 4, 5]
print(list)
for i in range(len(list)-1, 0, -1):
    j = random.randint(0, i + 1)
    list[i], list[j] = list[j], list[i]
print(list)
