# 2. Создайте программу для игры с конфетами человек против человека.

# Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга. Первый ход определяется
#  жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему
#  последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'
import random
print('Игра с конфетами')
print('Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга.\n\n'
      'Первый ход определяется жеребьёвкой.За один ход можно забрать не более чем 28 конфет.\n\n'
      'Все конфеты оппонента достаются сделавшему последний ход.\n')

allSweets = 150
sweetsOnTable = 150
maxCountSweet = 28
stepSweet = 0
whosStep = 0


def PlayTwoMans():
    sweetsOnTable = 150
    maxCountSweet = 28
    
    whosStep = 0
    player1_name = input('Игрок 1, как вас зовут? ')
    player2_name = input('Игрок 2, ваше имя? ')
    print('ok, начинаем игру\n')
    print('Первый ход определяем жеребьевкой.\n')
    

    if random.randint(1, 3) == 1:
        print(f'Итак, первый ходит: {player1_name}')
       
        whosStep = 0
    else:
        print(f'Итак, первый ходит:  {player2_name}')
        
        whosStep = 1

    while sweetsOnTable > 0:
        if whosStep == 0:

            print(f'На столе {sweetsOnTable} конфет(ы)')
            step = int(input(f'Твой ход, {player1_name}: '))
            if step > sweetsOnTable or step > maxCountSweet:
                print(
                    'За один ход можно забрать не более чем 28 конфет или не больше, чем осталось на столе \nПопробуй еще раз')
                step = int(input(f'{player1_name} Сколько конфет ты берешь?'))
            sweetsOnTable -= step
            if sweetsOnTable > 0:
                print('Продолжаем играть')
                whosStep = 1
            else:
                print('Конфет больше нет!')
                
        if whosStep == 1:

            print(f'На столе {sweetsOnTable} конфет(ы)')
            step = int(input(f'Твой ход, {player2_name}: '))
            if step > sweetsOnTable or step > maxCountSweet:
                print(
                    'За один ход можно забрать не более чем 28 конфет или не больше, чем осталось на столе \nПопробуй еще раз')
                step = int(input(f'{player2_name} Твой шаг:'))
            sweetsOnTable -= step
            if sweetsOnTable > 0:
                print('Продолжаем играть')
                whosStep = 0
            else:
                print('Конфет больше нет!')
                
    
    if sweetsOnTable == 0:
        
        if whosStep == 0:
            print(f'В нашей игре победил игрок {player1_name}. Поздравляем!!!')
        if whosStep == 1:
            print(f'В нашей игре победил игрок {player2_name}. Поздравляем!!!')


#PlayTwoMans()

def PlayToClevetBot():
    sweetsOnTable = 150
    maxCountSweet = 28
    sweetPlayer=0
    whosStep = 0
    player1_name = input('Игрок 1, как вас зовут? ')
    player2_name = 'Clever Bot'
    print(f'ok, начинаем игру c {player2_name}\n')
    print('Первый ход определяем жеребьевкой.\n')
    hod=0

    if random.randint(1, 3) == 1:
        print(f'Итак, первый ходит: {player1_name}')
        whosStep = 0
        hod=1
    else:
        print(f'Итак, первый ходит:  {player2_name}')
        whosStep = 1 #
        hod=1

    while sweetsOnTable > 0:
        if whosStep == 0 and hod==1:

            print(f'На столе {sweetsOnTable} конфет(ы)')
            step = int(input(f'Твой ход, {player1_name}: '))
            if step > sweetsOnTable or step > maxCountSweet:
                print(
                    'За один ход можно забрать не более чем 28 конфет или не больше, чем осталось на столе \nПопробуй еще раз')
                step = int(input(f'{player1_name} Сколько конфет ты берешь?'))
            sweetPlayer=step
            hod+=1
            sweetsOnTable -= step
            if sweetsOnTable > 0:
                print('Продолжаем играть')
                whosStep = 1
            else:
                print('Конфет больше нет!')
        if whosStep == 0 and hod>1:

            print(f'На столе {sweetsOnTable} конфет(ы)')
            step = int(input(f'Твой ход, {player1_name}: '))
            if step > sweetsOnTable or step > maxCountSweet:
                print(
                    'За один ход можно забрать не более чем 28 конфет или не больше, чем осталось на столе \nПопробуй еще раз')
                step = int(input(f'{player1_name} Сколько конфет ты берешь?'))
            sweetPlayer=step
            hod+=1
            sweetsOnTable -= step
            if sweetsOnTable > 0:
                print('Продолжаем играть')
                whosStep = 1
            else:
                print('Конфет больше нет!')       
        if whosStep == 1 and hod==1:#bot

            print(f'На столе {sweetsOnTable} конфет(ы).Ходит {player2_name}')
            step =  sweetsOnTable%29
            print(f'{player2_name} берет {step} конфет')
            sweetsOnTable -= step
            hod+=1
            whosStep = 0
           
        if whosStep == 1 and hod>1:#bot
            print(f'На столе {sweetsOnTable} конфет(ы).Ходит {player2_name}')
            # if sweetsOnTable>100:
            #     step =  random.randint(1,29)
            # elif sweetsOnTable>29:
            #     step =  29-sweetPlayer
            
            step =  29-sweetPlayer
            print(f'{player2_name} берет {step} конфет')
            sweetsOnTable -= step
            hod+=1
            if sweetsOnTable > 0:
                print('Продолжаем играть')
                whosStep = 0
            else:
                print('Конфет больше нет!')
            
                
    
    if sweetsOnTable == 0:
        
        if whosStep == 0:
            print(f'В нашей игре победил игрок {player1_name}. Поздравляем!!!')
        if whosStep == 1:
            print(f'В нашей игре победил игрок {player2_name}. К сожалению, вы,{player1_name} \n Попытайтесь еще раз')

PlayToClevetBot()
