# 1. Задайте рандомно список из чисел размером N, где N число с клавиатуры. Напишите программу,
#  которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint as rI
number = int(input("Введите размер списка: "))
summElem = 0
listRnd = [(lambda x:rI(-10, 10))(x) for x in range(number)]
print("Получившийся рандомный список:")
print(listRnd)
tup = list(enumerate(listRnd, start=0))
# print(tup)
summElem = sum([(lambda i: i[1])(i) for i in tup if i[0] % 2 == 1])

print(f'Сумма элементов на нечетных позициях: {summElem}')
