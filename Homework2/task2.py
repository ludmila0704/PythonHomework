# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

print('Введите число:')
number = int(input())
list_num = []

Fact_num = 1
for i in range(1, number+1):
    Fact_num = Fact_num*i
    list_num.append(Fact_num)

print(f'Набор произведений чисел от 1 до {number}: \n{list_num}')
