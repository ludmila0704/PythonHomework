#Реализуйте алгоритм перемешивания списка.

from random import random
from random import randint

list_num=[]

for i in range(10):
    list_num.append(randint(-10,10))
print(list_num)
list_num1=[]
list_num1=list_num.copy()

for i in range(int(len(list_num)/2)):
    temp=list_num[i]
    #print(temp)
    list_num1[i]=list_num[len(list_num)-1-i]
    #print(f'list_num1[i] {list_num1[i]}')
    list_num1[len(list_num1)-1-i]=temp

print(list_num1)