""" Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму. """
k = int(input('Введите число k'))
sum = 0
for i in range(k):
    sum += round((1+1/k)**k, 1)
print(f'Cумма равна {sum}')