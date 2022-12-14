# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
#  6 -> да
#  7 -> да
#  1 -> нет

week_number = int(input('Введите число дня недели:'))
list_num = [i for i in range(1, 8)]
list_w = ['Понедельник - рабочий день', 'Вторник - рабочий день', 'Среда - рабочий день',
          'Четверг - рабочий день', 'Пятница - рабочий день', 'Суббота - выходной день', 'Воскресенье - выходной день']
print(list_num)
zip_w = list(zip(list_num, list_w))

if week_number in list_num:

    elem =[(lambda week_n: i[1])(week_number)
            for i in zip_w if i[0] == week_number]
    print((elem))
else:
    print('Введите верное число дня недели!')
