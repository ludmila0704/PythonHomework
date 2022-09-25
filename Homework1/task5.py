#Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

import re

#определяем массивы предикатов x, y, z
x_list = [0, 0, 0, 0, 1, 1, 1, 1]
y_list = [0, 0, 1, 1, 0, 0, 1, 1]
z_list = [0, 1, 0, 1, 0, 1, 0, 1]

print('X','  ','Y','  ','Z','  ','¬(X ⋁ Y ⋁ Z)','  ','¬X ⋀ ¬Y ⋀ ¬Z')
print('-------------------------------------------')
for i in range(len(x_list)):
    left_expression = not (x_list[i] or y_list[i] or z_list[i]) #левая часть утверждения
    right_expression = (not x_list[i]) and (not y_list[i]) and (not z_list[i])  #правая часть утверждения
    print(x_list[i],'  ',y_list[i],'  ',z_list[i],'   ',left_expression,'        ',right_expression)

print('Выражение истинно, если левая и правая части утверждения равны для всех значений предикат.')
