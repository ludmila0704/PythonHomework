# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0

#from fileinput import filename


pathRead1 = r"D:\Python\Homework\Homework4\eq1task5.txt"
pathRead2 = r"D:\Python\Homework\Homework4\eq2task5.txt"
pathWriteF = r"D:\Python\Homework\Homework4\eqfinaltask5.txt"


string = ""
finalWord = {}


def readFile():

    try:
        with open(fileDir, 'r') as data:
            file = data.read().split(" ")

    except:
        print("Ошибка работы с файлом")
    return file


def writeFile():

    try:
        with open(fileDir, 'w') as data:
            data.write(finalEquation)

    except:
        print("Ошибка работы с файлом")


def readEquation():
    firstEquation = string

    eqation = {}
    firstEquation = firstEquation.replace(
        "+", " +").replace("-", " -")[:-2].split()

    for i in range(len(firstEquation)):
        firstEquation[i] = firstEquation[i].replace("+", "").split("x^")
        eqation[int(firstEquation[i][1])] = int(firstEquation[i][0])

    return eqation


fileDir = pathRead1
stringFile = readFile()
for elem in stringFile:
    string += elem
print(f'Первый многочлен: {string}')
word1 = readEquation()

fileDir = pathRead2

string = ""
stringFile2 = readFile()
for elem in stringFile2:
    string += elem
print(f'Второй многочлен: {string}')
word2 = readEquation()
# print(word1)
# print(word2)


for i in range(max(len(word1), len(word2)), -1, -1):
    first = word1.get(i)
    second = word2.get(i)
    if first != None or second != None:
        finalWord[i] = (first if first != None else 0) + \
            (second if second != None else 0)

print(f'Словарь сложения двух уравнений (степень:коэффициент): \n{finalWord}')
finalEquation = ""
for k in finalWord.items():

    if k[0] == max(finalWord.keys()):
        if k[1] > 0:
            finalEquation += str(int(k[1]))+'x^'+str(int(k[0]))
        if k[1] < 0:
            finalEquation += '-' + str(abs(int(k[1])))+'x^'+str(int(k[0]))
    else:

        if k[1] > 0:
            finalEquation += ' + ' + str(int(k[1]))+'x^'+str(int(k[0]))
        if k[1] < 0:
            finalEquation += ' - '+str(abs(int(k[1])))+'x^'+str(int(k[0]))


finalEquation = finalEquation + ' = 0'
print("Результат сложения двух многочленов:")
print(finalEquation.replace('x^1', 'x').replace('x^0', '').replace('1x^', 'x^'))
fileDir = pathWriteF
writeFile()
