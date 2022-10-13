# 3. Создайте программу для игры в 'Крестики-нолики'.

listIndexBoard = []
for i in range(1, 10):
    listIndexBoard.append(i)
victoryList = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
               (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))  # победные значения
print('Начинаем игру "Крестики-нолики"\n')
print(f'{listIndexBoard[0]:^5}|{listIndexBoard[1]:^5}|{listIndexBoard[2]:^5}|')
print('-------------------')
print(f'{listIndexBoard[3]:^5}|{listIndexBoard[4]:^5}|{listIndexBoard[5]:^5}|')
print('-------------------')
print(f'{listIndexBoard[6]:^5}|{listIndexBoard[7]:^5}|{listIndexBoard[8]:^5}|')
print('-------------------')
sign = "O"
viktory = ''
step = 0
while viktory == '':

    if sign == "O":
        sign = "X"
    else:
        sign = "O"

    index = int(input(f'\n\n ход {"игрока" if sign=="X" else "противника"}: '))
    if index >= 1 and index <= 9:
        if (str(listIndexBoard[index-1]) not in "XO"):
            listIndexBoard[index-1] = sign
            step += 1
            
        else:
            print("Эта клетка уже заполнена. ")
    else:
        print("Такой позиции нет. Введи нужную позицию от 1 до 9")

    print(
        f'{listIndexBoard[0]:^5}|{listIndexBoard[1]:^5}|{listIndexBoard[2]:^5}|')
    print('-------------------')
    print(
        f'{listIndexBoard[3]:^5}|{listIndexBoard[4]:^5}|{listIndexBoard[5]:^5}|')
    print('-------------------')
    print(
        f'{listIndexBoard[6]:^5}|{listIndexBoard[7]:^5}|{listIndexBoard[8]:^5}|')
    print('-------------------')

    if step < 8:
        for v in victoryList:
            if listIndexBoard[v[0]] == listIndexBoard[v[1]] == listIndexBoard[v[2]]:
                viktory = listIndexBoard[v[0]]

                print(f'Победил игрок {viktory} Поздравляем!')
    
    else:
        viktory = "Ничья"
        print(f'{viktory}!')

    
