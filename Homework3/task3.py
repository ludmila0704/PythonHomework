# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
#  максимальным и минимальным значением дробной части элементов.
# ВАЖНО: если число целое, то оно не имеет дробной части и засчитывать 0 как минимальное не стоит
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import math
number = int(input("Введите размер списка из вещественных чисел: "))
floatList = []
for i in range(number):
    floatList.append(float(input(f"Введите {i+1} элемент: ")))

print(floatList)
newList = []

# количество знаков после запятой в вещественном числе


def Count_sign(num):
    count = 0
    div = 1
    while True:
        if not (num*div == int(num*div)):
            count += 1
            div *= 10
        else:
            break
    return count

#Создаем массив дробных частей
for i in range(len(floatList)):
    d = (floatList[i] % 1)

    if d > 0.0:#если 0, не берем в массив
        newList.append(round(d, Count_sign(floatList[i])))

#ищем мин и макс значение 
maxFloat = minFloat = newList[0]
for i in range(len(newList)):
    if newList[i] > maxFloat:
        maxFloat = newList[i]
    if newList[i] < minFloat:
        minFloat = newList[i]
#сравниваем количество знаков после запятой для мин и мах, чтобы правильно вычесть
if Count_sign(maxFloat) > Count_sign(minFloat):
    count_round = Count_sign(maxFloat)
else:
    count_round = Count_sign(minFloat)

res = round(maxFloat-minFloat, count_round)
print(
    f'Разница между максимальным и минимальным значением дробной части элементов: {res}')


# решение через строки
# newList = []
# for i in floatList:
#     if (".") in i:
#         k = i.find(".")
#         newList.append(int(i[k+1::]))

# print(newList)
# maxFloat = minFloat = newList[0]
# for i in range(len(newList)):
#     if newList[i] > maxFloat:
#         maxFloat = newList[i]
#     if newList[i] < minFloat and newList[i] != 0:
#         minFloat = newList[i]
# res = "0."+str(maxFloat-minFloat)

# print(
#     f'Разница между максимальным и минимальным значением дробной части элементов: {res}')
