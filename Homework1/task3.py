#Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.
print('Введите число:')
number = float(input())

if (number % 5 ==0 and number % 10 == 0 and number % 15 == 0) and number % 30 !=0:
    print('да')
else:
    print('нет')
