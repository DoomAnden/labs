# Формируется матрица F следующим образом: если в С количество чисел, больших К в нечетных столбцах в области 3 больше,
# чем произведение чисел в нечетных строках в области 2, то поменять в В симметрично области 1 и 3 местами, иначе С и Е
# поменять местами несимметрично. При этом матрица А не меняется. После чего вычисляется выражение: ((К*A)*F+ K* F T .
# Выводятся по мере формирования А, F и все матричные операции последовательно.
import random


def print_matrix(matrix):
  for row in matrix:
    for elem in row:
      print('{:4}'.format(elem), end=' ')
    print()


def paste_matrix(matrix_F, matrix, column_index, row_index):
  a = column_index
  for row in matrix:
    for element in row:
      matrix_F[row_index][column_index] = element
      column_index += 1
    row_index += 1
    column_index = a


def matrix_zero(size):
        return [[0 for i in range(size)] for j in range(size)]


def matrix_input(matrix, i1, i2, j1, j2):
    zer_matrix = matrix_zero(len(matrix)//2)
    for i in range(i1, i2):
        for j in range(j1, j2):
            zer_matrix[i - i1][j - j1] = matrix[i][j]
    return zer_matrix


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
        ans = input('Для использование единичной матрицы напишите 1, для использования случайно сгенерированной напишите 2: ')
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


koll, multi = 1, 0
for i in range(n // 4, half_n):
    for j in range(half_n - i - 1, i + 1):
        if matC[i][j] > K and (j + 1) % 2 != 0:
            koll += 1

print('Количество чисел, больших К в нечетных столбцах в области 3:', koll)

for i in range(n // 4, half_n):
    for j in range(half_n - i - 1, i + 1):
        if (j + 1) % 2 != 0:
            multi *= matC[j][i]

print('Произведение чисел в нечетных строках в области 2:', multi)


if koll > multi:
    print('Начальная подматрциа B:')
    print_matrix(matB)
    for i in range(n // 4, half_n):
        for j in range(half_n - i - 1, i + 1):
            matB[i][j], matB[((n // 4) + 1) - i][j] = matB[((n // 4) + 1) - i][j], matB[i][j]
    print('Получившаяся подматрица B:')
    print_matrix(matB)
else:
    matrix_E, matrix_C = matC, matE

matrix_F = matA.copy()
paste_matrix(matrix_F, matE, 0, 0)
paste_matrix(matrix_F, matB, fix_n, 0)
paste_matrix(matrix_F, matC, fix_n, fix_n)
paste_matrix(matrix_F, matD, 0, fix_n)

print('Матрица F:')
print_matrix(matrix_F)

matrix_F_transp = matrix_zero(n)

print("Матрица F транспонированая:")
for i in range(n):
    for j in range(n):
        matrix_F_transp[i][j] = matrix_F[j][i]
print_matrix(matrix_F_transp)

print('Вычислим ((К*A)*F+ K* F T:')
matKAF = matrix_zero(n)
matAK = matA.copy()
matres = matrix_zero(n)
matFT = matrix_F_transp.copy()

for i in range(n):
    for j in range(n):
        matAK[i][j] *= K
print('Результат K * A:')
print_matrix(matAK)

for i in range(n):
    for j in range(n):
        for k in range(n):
            matKAF[i][j] += matA[i][k] * matrix_F[k][j]
print('Результат (К*A)*F:')
print_matrix(matKAF)

for i in range(n):
    for j in range(n):
        matFT[i][j] *= K
print('Результат K * FT:')
print_matrix(matFT)



for i in range(n):
    for j in range(n):
        matres[i][j] = matKAF[i][j] + matFT[i][j]
print('Результат:')
print_matrix(matres)
