# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму
print('Введите количество элементов последовательности:')
number = int(input())
list_num = []


Summ_num_elem = 0
for i in range(1, number+1):
    elem_list = round((1+1/i)**i, 2)
    list_num.append(elem_list)
    Summ_num_elem += elem_list

print(f'Последовательность: {list_num}: \nЕе сумма равна {Summ_num_elem}')
