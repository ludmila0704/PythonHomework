#Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

import re


# print('Введите число X:')
# x_predicate = int(input())
# print('Введите число Y:')
# y_predicate = int(input())
# print('Введите число Z:')
# z_predicate = int(input())


# left_expression = not (x_predicate or y_predicate or z_predicate)
# right_expression = not x_predicate and not y_predicate and not z_predicate
# result = left_expression == right_expression

# if result:
#    print('Выражение истинно')
# else:
#    print('Выражение ложно')
def inputNumbers(x):
    xyz = ["X", "Y", "Z"]
    a = []
    for i in range(x):
        a.append(input(f"Введите значение {xyz[i]}: "))
    return a


def checkPredicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result


statement = inputNumbers(3)

if checkPredicate(statement) == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")