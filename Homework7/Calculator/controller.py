import logger
import model
import view




def get_operation(list_oper,i,oper):
     
    if list_oper[i]==oper:
        list_oper[i-1]=model.oper_dict.get(oper)(int(list_oper[i-1]),int(list_oper[i+1]))
        
        delete_el(list_oper,i)
        return True
    return False

def delete_el(string,i):
    string.pop(i)
    string.pop(i)

def string_calculation(list_oper:list):
    while len(list_oper)>1:
        
        if '*' in list_oper or '/' in list_oper:
            for i in range(len(list_oper)):
                if get_operation(list_oper,i,'*'):break
                if get_operation(list_oper,i,'/'):break
        elif '+' in list_oper or '-' in list_oper:
            for i in range(len(list_oper)):
                if get_operation(list_oper,i,'+'):break
                if get_operation(list_oper,i,'-'):break
    
    return list_oper
          


def exp_split(exp:str):
    exp=model.string_parse(exp)
    while len(exp)>1:
        exp=string_calculation(exp)
    model.total=exp[0]
    logger.logger(f'{model.string_oper} = {model.total}')

