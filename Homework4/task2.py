# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
number = int(input("Введите натуральное число N: "))
listMn = []


def Single_mn(num):
    i = 2
    while (num) > 2:

        if num % i == 0:
            num = num//i
            listMn.append(i)
        else:
            i += 1

    return listMn


Single_mn(number)
print(f'Простые множители натурального числа {number}: \n{listMn}')
