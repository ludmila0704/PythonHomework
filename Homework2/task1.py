# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11
print('Введите число:')

number = float(input())
#выделяем целую часть числа
#if float.is_integer( number ):
if number % 1==0:
    number=int(number)
    summ=0
    while (number > 0):
        summ = int(summ + number % 10)
        number = number / 10
    print(f' Сумма цифр числа равна {int(summ)} ')
else:
    d = (round( number % 1),2 )
    print(f'd  {d} ')
    summ=0
   # while(d!=0):
    #d = int(( number % 1) * 10)
    d = (d * 10)
    print(f'd  {d} ')
        
    #summ=summ+d
    #d=d-int(d)
    print(f'd  {d} ')



    print(f'Сумма цифр числа равна  {d} равна {summ}')
#not isinstance(number,float)


