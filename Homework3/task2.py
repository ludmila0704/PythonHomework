# Напишите программу, которая найдёт произведение пар чисел списка
# (Список создаем как в предыдущем задании). Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# *Пример:*
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random

number = int(input("Введите размер списка: "))
listRnd = []

for i in range(number):
    listRnd.append(random.randint(0, 10))
print(listRnd)
listNew = []


def Composition(list):

    for i in range(int(len(list)/2)):
        listNew.append(list[i]*list[len(list)-1-i])

    if len(list) % 2 == 1:
        listNew.append(list[int(len(list)/2)]**2)
    return listNew


Composition(listRnd)
print(f'Список произведений пар рандомного списка: \n{listNew}')
