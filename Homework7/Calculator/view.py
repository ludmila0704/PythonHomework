import logger
import model


def error_value():
    logger.logger('Ошибка ввода данных')
    return print('Ошибка ввода данных')

def error_zero():
    return print('На ноль делить нельзя!')


def print_total():
    if model.total== None:
        error_value()
    else:    
        return print(f'Результат: {model.total}')

