import random

def MyMatrix(n,m,minCount, maxCount):
    matrix = []
    for i in range(n):
        stroki = []
        for j in range(m):
            num = random.randint(minCount,maxCount)
            stroki.append(num)
        matrix.append(stroki)
    return matrix

n = int(input("Введите число строк:"))
m = int(input("Введите число столбцов:"))
maxCount = int(input("Введите максимальное число:"))
minCount = int(input("Введите минимальное число:"))
if n < 0:
    print("Количество строк не может быть отрицательным")
if m < 0:
    print("Количество столбцов не может быть отрицательным")
if maxCount >= minCount:
    Newmatrix = MyMatrix(n,m,minCount,maxCount)
    for stroki in Newmatrix:
        print(stroki)
else:
    minn = 0
    maxx = 0
    minCount = minn
    minn = maxx
    maxx = minCount
    print("Максимальное значение не может быть больше минимального,"
    "значения были автоматически поменяны местами!")
    Newmatrix = MyMatrix(n, m, minCount, maxCount)
for stroki in Newmatrix:
    print(stroki)