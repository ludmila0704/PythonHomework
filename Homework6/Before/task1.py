# 1. Задайте рандомно список из чисел размером N, где N число с клавиатуры. Напишите программу,
#  которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# import random

# number = int(input("Введите размер списка: "))
# listRnd = []

# for i in range(number):
#     listRnd.append(random.randint(-10, 10))
# print(listRnd)

# summElem = 0
# print('На нечетных позициях элементы: ', end=" ")
# for i in range(len(listRnd)):
#     if i % 2 == 1:
#         summElem = listRnd[i] + summElem
#         print(listRnd[i], end=", ")

# print(f'их сумма: {summElem}')
