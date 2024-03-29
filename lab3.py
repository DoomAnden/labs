# Формируется матрица F следующим образом: если в С количество чисел, больших К в нечетных столбцах в области 3 больше,
# чем произведение чисел в нечетных строках в области 2, то поменять в В симметрично области 2 и 3 местами, иначе С и Е
# поменять местами несимметрично. При этом матрица А не меняется. После чего вычисляется выражение: ((К*A)*F+ K* F T .
# Выводятся по мере формирования А, F и все матричные операции последовательно.

import random


def print_matrix(mat):
    for row in mat:
        for elem in row:
          print('{:4}'.format(elem), end=' ')
        print()


def pastemat(matF, matrix, column_index, row_index):
    a = column_index
    for row in matrix:
      for element in row:
        matF[row_index][column_index] = element
        column_index += 1
      row_index += 1
      column_index = a


def matzero(size):
    return [[0 for i in range(size)] for j in range(size)]


def matrix_input(mat, i1, i2, j1, j2):
    zero_mat = matzero(len(mat)//2)
    for i in range(i1, i2):
        for j in range(j1, j2):
            zero_mat[i - i1][j - j1] = mat[i][j]
    return zero_mat


try:
    K = int(input('Введите число K: '))
    n = int(input('Введите число число N, больше или равное 5: '))
    while n < 5:
        n = int(input('Введите число N, большее или равное 5: '))
except ValueError:
    print('Введенный символ не является числом.')
    exit(0)

ans = input('Для использование единичной матрицы напишите 1, для использования случайно сгенерированной напишите 2: ')
if ans not in ['1', '2']:
    print('Попробуйте ещё')
    while ans not in ['1', '2']:
        n = int(input('Для использование единичной матрицы напишите 1, для использования случайно сгенерированной напишите 2: '))
if ans == '1':
    matA = [[(1) for i in range(n)] for j in range(n)]
elif ans == '2':
    matA = [[random.randint(-10, 10) for i in range(n)] for j in range(n)]


print('Матрица А изначальная:')
print_matrix(matA)

half_n = n//2
fix_n = half_n
if n % 2 != 0:
    fix_n += 1

matB = matrix_input(matA, 0, half_n, fix_n, n)
matC = matrix_input(matA, fix_n, n, fix_n, n)
matD = matrix_input(matA, fix_n, n, 0, half_n)
matE = matrix_input(matA, 0, half_n, 0, half_n)

print('Подматрицы матрицы A:')
print('Подматрица B')
print_matrix(matB)
print('Подматрица С')
print_matrix(matC)
print('Подматрица D')
print_matrix(matD)
print('Подматрица E')
print_matrix(matE)

pro, koll = 1, 0
for i in range(n // 4, half_n):
    for j in range(half_n - i - 1, i + 1):
        if j % 2 != 0:
            if matC[i][j] > K:
                koll += 1
print('количество чисел, больших К в нечетных столбцах в области 3:', koll)


for i in range(n // 4, half_n):
    for j in range(half_n - i - 1, i + 1):
        if j % 2 != 0:
            pro *= matC[j][i]
print('произведение чисел в нечетных строках в области 2:', pro)


if koll > pro:
    print('количество чисел, больших К в нечетных столбцах в области 3 больше, чем произведение чисел в нечетных строках в области 2')
    print('Начальная подматрциа B:')
    print_matrix(matB)
    for i in range(n // 4, half_n):
        for j in range(half_n - i - 1, i + 1):
            matB[i][j], matB[j][i] = matB[j][i], matB[i][j]
    print('Получившаяся подматрица С:')
    print_matrix(matC)
else:
    print('количество чисел, больших К в нечетных столбцах в области 3 меньше, чем произведение чисел в нечетных строках в области 2')
    matrix_E, matrix_C = matC, matE

matF = matA.copy()
pastemat(matF, matE, 0, 0)
pastemat(matF, matB, fix_n, 0)
pastemat(matF, matC, fix_n, fix_n)
pastemat(matF, matD, 0, fix_n)

print('Матрица F:')
print_matrix(matF)

matFt = matzero(n)

print("Матрица F транспонированая:")
for i in range(n):
    for j in range(n):
        matFt[i][j] = matF[j][i]
print_matrix(matFt)

matKAF = matzero(n)
matKA = matA.copy()
matTF = matFt.copy()
print('Вычисляем (К * A) * F + K * FT:')

for i in range(n):
    for j in range(n):
        matKA[i][j] *= K

print('Результат K * A:')

for i in range(n):
    for j in range(n):
        matTF[i][j] *= K

print('Результат K * FT:')


for i in range(n):
    for j in range(n):
        for k in range(n):
            matKAF[i][j] += matKA[i][k] * matF[k][j]
print('Результат A * F:')
print_matrix(matKAF)


print_matrix(matTF)
matres = matzero(n)
for i in range(n):
    for j in range(n):
        matres[i][j] = matKAF[i][j] + matTF[i][j]
print('Результат:')
print_matrix(matres)