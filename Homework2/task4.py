# Реализуйте алгоритм перемешивания списка.

from random import random
from random import randint

list_num = []

for i in range(10):
    list_num.append(randint(0, 20))
print("Первоначальный список:")
print(list_num)
list_num1 = []
list_num1 = list_num.copy()
# мешаем список первый раз-выводим элементы в обратном порядке, с конца списка
for i in range(len(list_num)):
    temp = list_num[i]
    list_num1[i] = list_num[len(list_num)-1-i]
    list_num1[len(list_num1)-1-i] = temp

print("Первое перемешивание:")
print(list_num1)
# мешаем второй раз- меняем местами элементы на нечетных позициях

for i in range(len(list_num1)-2):
    if (i % 2 != 0):
        temp = list_num1[i]
        list_num1[i] = list_num1[i+2]
        list_num1[i+2] = temp
        i += 4

print("Второе перемешивание:")
print(list_num1)
