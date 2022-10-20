
import controller
import view

total = 0
string_oper=''

oper_dict={
    "+": lambda x , y: int(x)+int(y),
    '-': lambda x , y: int(x)-int(y),
    '*': lambda x , y: int(x)*int(y),
    '/': lambda x , y: int(x)/int(y) if y!=0 else view.error_zero()
    }


def init_string_input():
    global string_oper
    string_oper = controller.input_string('Введите выражение: ')
    

def string_parse(string:str):
    string=string.replace(' ', '').strip()
    #print(string)
    string=string.replace('+',' + ')\
        .replace('-',' - ')\
        .replace('*',' * ')\
        .replace('/',' / ')
    list=string.split()
    
    return list


        