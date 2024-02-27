import random
import time
def MyMatrix(n, m, minCount, maxCount):
    matrix = []
    for i in range(n):
        stroki = []
        for j in range(m):
            num = random.randint(minCount, maxCount)
            stroki.append(num)
        matrix.append(stroki)
    return matrix

def Vibor_sort(matrix):
        for arr in matrix:
            n = len(arr)
            for i in range(n):
                min_idx = i
                for j in range(i + 1, n):
                    if arr[j] < arr[min_idx]:
                        minn= j
                arr[i], arr[minn] = arr[minn], arr[i]
def Vstavka_sort(arr):
    n = len(arr)
    for i in range(1, n):
        Elem = arr[i]
        j = i - 1
        while j >= 0 and  Elem  < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] =  Elem
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        propysk = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                propysk = True
        if not propysk:
            break
def shell_sort(arr):
    n = len(arr)
    razbien = n // 2
    while  razbien > 0:
        for i in range( razbien, n):
            temp = arr[i]
            j = i
            while j >=  razbien and arr[j - razbien] > temp:
                arr[j] = arr[j -  razbien]
                j -=  razbien
            arr[j] = temp
        razbien //= 2
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    razdelarr = arr[len(arr) // 2]
    left = [x for x in arr if x < razdelarr]
    middle = [x for x in arr if x == razdelarr]
    right = [x for x in arr if x > razdelarr]
    return quick_sort(left) + middle + quick_sort(right)

n = int(input("Введите число строк: "))
m = int(input("Введите число столбцов: "))
maxCount = int(input("Введите максимальное число: "))
minCount = int(input("Введите минимальное число: "))
Newmatrix = MyMatrix(n, m, minCount, maxCount)
###
print("Сгенерированная матрица:")
for stroki in Newmatrix:
    print(stroki)
#### Сортировка выбором
def Vibor():
    sortmatrix = [Copy[:] for Copy in Newmatrix]  #копия матрицы
    Vibor_sort(sortmatrix)
    print("Сортировка выбором:")
    for Copy in sortmatrix:
        print(Copy)
    start_time = time.time()
    print(f"--- {0} ms ---".format(round((time.time() - start_time) * 1000)))
###
def Vstavka():
    print("Сортировка вставкой:")
    for stroki in Newmatrix:
        Vstavka_sort(stroki)
    for stroki in Newmatrix:
        print(stroki)
    start_time = time.time()
    print(f"--- {0} ms ---".format(round((time.time() - start_time) * 1000)))

def bubble():
    print("Сортировка пузырьком:")
    for stroki in Newmatrix:
        bubble_sort(stroki)
    for stroki in Newmatrix:
        print(stroki)
    start_time = time.time()
    print(f"--- {0} ms ---".format(round((time.time() - start_time) * 1000)))
def Shell():
    print("Сортировка Шелла:")
    for stroki in Newmatrix:
        shell_sort(stroki)
    for stroki in Newmatrix:
        print(stroki)
    start_time = time.time()
    print(f"--- {0} ms ---".format(round((time.time() - start_time) * 1000)))
def quick():
    print("быстрая сортировка:")
    for stroki in Newmatrix:
        quick_sort(stroki)
    for stroki in Newmatrix:
        print(stroki)
    start_time = time.time()
    print(f"--- {0} ms ---".format(round((time.time() - start_time) * 1000)))
####
print(Vibor())
print(Vstavka())
print(bubble())
print(Shell())
print(quick())