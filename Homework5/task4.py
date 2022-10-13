# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример: aaaaaaabbbbbbccccccccc => 7a6b9c и 11a3b7c => aaaaaaaaaaabbbccccccc



pathRead = r"D:\Python\Homework\Homework5\task4input.txt"
pathWrite = r"D:\Python\Homework\Homework5\task4output.txt"


try:
    with open(pathRead, 'r') as data:
        textInput = data.read()  

except:
    print("Ошибка работы с файлом")


#textInput = 'aaaaaaabbbbbbccccccccc'
#textInput = '11a3b7c'
stringPrint = ''
print(f'Входные данные:\n{textInput}')
if textInput.isalpha():  

    alpha = textInput[0]  # запоминаем первый элемент
    count = 1
    for elem in textInput[1:]:

        if elem == alpha:
            count += 1

        else:
            stringPrint += str(count)+alpha
            alpha = elem
            count = 1

    stringPrint += str(count)+alpha
    print(f'Выходные данные:\n{stringPrint}')
else:
    digAlpha = ''
    for elem in textInput:
        if elem.isdigit():
            digAlpha += elem

        else:
            stringPrint += int(digAlpha)*elem
            digAlpha = ''
    print(f'Выходные данные:\n{stringPrint}')

try:
    with open(pathWrite, 'w') as data:
        data.write(stringPrint)

except:
    print("Ошибка работы с файлом")
