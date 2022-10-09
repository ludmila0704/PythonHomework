# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от-100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени

# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0
from random import randint as rI

pathWrite1 = r"D:\Python\Homework\Homework4\eq1task5.txt"
pathWrite2 = r"D:\Python\Homework\Homework4\eq2task5.txt"


def getEquation():
    degree_k = int(input("Введите натуральную степень: "))
    equation = ''

    for k in range(degree_k, -1, -1):
        coef = rI(-10, 10)

        if k == degree_k:
            if coef > 0:
                equation += str(coef)+'x^'+str(k)
            if coef < 0:
                equation += '-'+str(abs(coef)) + 'x^'+str(k)
        else:
            if coef > 0:
                equation += ' + '+str(coef)+'x^'+str(k)
            if coef < 0:
                equation += ' - ' + str(abs(coef)) + 'x^'+str(k)
    return equation + ' = 0'


#eq = getEquation()


try:
    with open(pathWrite1, 'w') as data:
        data.write(getEquation())

except:
    print("Ошибка работы с файлом")

try:
    with open(pathWrite2, 'w') as data:
        data.write(getEquation())

except:
    print("Ошибка работы с файлом")


#print((eq.replace('x^1', 'x').replace('x^0', '').replace('1x^', 'x^')))
