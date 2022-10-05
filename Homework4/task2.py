#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
number = int(input("Введите натуральное число N: "))
listMn = []

def Single_mn(num):

    for i in range(1,num+1):
        if num%i==0:
            listMn.append(i)
            num=num//i
            #Single_mn(num)
    return listMn        

Single_mn(number)
# for i in range(1,number+1):
#     if number%i==0:
#         listMn.append(i)
#         number=number//i
print(listMn)
