"""     Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

    Пример:
- 0,56 -> 11
 """

n = input('Введите вещественное число --> ')
#n = '12,56534343'
sum = 0

for i in range(len(n)):
    if n[i] != ",":
        sum += int(n[i])
print(f'Сумма цифр числа {n} равна {sum}')
