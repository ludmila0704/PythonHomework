# 5. Задайте число - размер списка. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

number = int(input("Введите размер списка: "))


def Fibonacchi(num):
    if num in [1, 2]:
        return 1
    elif num > 0:
        return Fibonacchi(num-1)+Fibonacchi(num-2)
    else:
        return Fibonacchi(num+2)-Fibonacchi(num+1)


listFibonacci = []


for i in range(-number, number+1, 1):
    listFibonacci.append(Fibonacchi(i))
print(
    f'Список чисел Фибоначчи, в том числе для отрицательных индексов: \n{listFibonacci}')
