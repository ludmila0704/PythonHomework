# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт 
# номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
#  x=34; y=-30 -> 4
#  x=2; y=4-> 1
#  x=-34; y=-30 -> 3
print('Введите координаты точки Х (X # 0):')
xx= int (input())
print('Введите координаты точки Y (Y # 0):')
yy= int (input())
if xx != 0 and yy !=0: 
    if xx > 0 and yy > 0:
        print (f'Точка с координатами ({xx}:{yy}) принадлежит 1 четверти')
    if xx < 0 and yy > 0:
        print (f'Точка с координатами ({xx}:{yy}) принадлежит 2 четверти')
    if xx < 0 and yy < 0:
        print (f'Точка с координатами ({xx}:{yy}) принадлежит 3 четверти')
    if xx > 0 and yy < 0:
        print (f'Точка с координатами ({xx}:{yy}) принадлежит 4 четверти')
else:
    print('Неверно введены координаты!')