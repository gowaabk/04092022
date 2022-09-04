""" Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных пользователем через пробел позициях.

 """

import random


n = int(input('Введите размер списка N --> '))

spisok = []
for i in range(n):
    spisok.append(random.randint(-n, n))
print(spisok)
index = input('Введите индексы элемента через пробел -->')

x = int(index.split(' ')[0])
y = int(index.split(' ')[1])

print(f'Произведение равно {spisok[x]*spisok[y]}')
