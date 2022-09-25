# Напишите программу, которая принимает на вход координаты двух точек и находит
#  расстояние между ними в 2D пространстве.
# Пример:
#  A (3,6); B (2,1) -> 5,09
#  A (7,-5); B (1,-1) -> 7,21

from cmath import sqrt
#import cmath


print('Введите координаты первой точки  X1:=')
x_firstpoint= int (input())
print('Введите координаты первой точки  Y1:=')
y_firstpoint= int (input())
print('Введите координаты второй точки  X2:=')
x_secondpoint= int (input())
print('Введите координаты второй точки  Y2:=')
y_secondpoint= int (input())

distance_points = sqrt((x_secondpoint-x_firstpoint)**2+(y_secondpoint-y_firstpoint)**2)
distance_points = round (distance_points.real, 2)
print(f'Расстояние между первой точкой с координатами ({x_firstpoint}:{y_firstpoint}) и второй точкой с координатами ({x_secondpoint}:{y_secondpoint}) равно {distance_points}')