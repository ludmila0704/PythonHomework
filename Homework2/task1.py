# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11
print('Введите число:')
number = float(input())

#считаем сумму цифр целой части числа 
numberint=int(number)
summint=0
while (numberint > 0):
    summint = int(summint + numberint % 10)
    numberint = numberint / 10
print(f' Сумма цифр числа равна {int(summint)} ')
#считаем сумму цифр дробной части числа 
d = number % 1
d.as_integer_ratio()

summ_ost=0
d1=d
while(d1!=0 and d1!=9):
    
    d1 = int(d * 10) # целое   
    summ_ost=summ_ost+d1
    d2=d*10-d1
    d=d2
    if int(d2*10)==9:#пайтон добавляет 9, поэтому это условие
        summ_ost+=1
        break
#если входная 9 считает неверно
summ=summint+summ_ost
print(f'Сумма цифр числа {number} равна {summ}')

