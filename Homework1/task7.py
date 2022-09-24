# программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

print('Введите номер четверти (1,2,3,4):')
quarter = int (input())

if quarter == 1: 
    print (f'В {quarter} четверти х > 0, y > 0')
elif quarter == 2: 
    print (f'В {quarter} четверти х < 0, y > 0')
elif quarter == 3: 
    print (f'В {quarter} четверти х < 0, y < 0')
elif quarter == 4: 
    print (f'В {quarter} четверти х > 0, y < 0')
else:
    print('Неверно введен номер четверти!')