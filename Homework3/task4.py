# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# 45 -> 101101
# 3 -> 11
# 2 -> 10
#     print(f"Число {num} в двоичной системе это {binum})
number = int(input("Введите десятичное число: "))
listBin = []


def Binum(num):
    res = ""
    while (num > 0):
        res += str(num % 2)
        num //= 2

    return res


res = Binum(number)

print(f'Число {number} в двоичной системе это {res[::-1]}')
