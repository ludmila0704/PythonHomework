# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# Примеры:
# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

print('Введите число:')
number = int(input())

print(f'Числа от {-number} до {number}:')
for i in range(-number, number+1,1):
    print( i, end="  ")
    
