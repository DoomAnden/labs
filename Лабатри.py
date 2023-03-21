# Формируется матрица F следующим образом: если в С сумма чисел, по периметру области 3 больше,
# чем произведение чисел по периметру области 2, то поменять в С симметрично области 2 и 3 местами,
# иначе В и Е поменять местами несимметрично. При этом матрица А не меняется.
# После чего вычисляется выражение: A*F+ K*F T . Выводятся по мере формирования А,
# F и все матричные операции последовательно.
import random


def fill_matrix(a, n, zero=-1):
    if zero == -1:
        for i in range(n):
            row = []
            for j in range(n):
                row.append(random.randint(-10, 10))
            a.append(row)
    if zero == 0:
        for i in range(n):
            row = []
            for j in range(N):
                row.append(0)
            a.append(row)


def mat_print(a, n):
    for i in range(n):
        print(a[i])


K = int(input('Введите K: '))
N = int(input('Введите N: '))

if (N % 2 != 0) or ((N / 2) % 2 == 0):
    print('Неверные исходные данные. Число N должно быть четным, причем N/2 должно быть нечетным')
    exit()

B, C, D, E, A, F, FA, Ft, FinalMat = [], [], [], [], [], [], [], [], []
n = N // 2
summ_43 = 0
summ_42 = 0


fill_matrix(B, n)
fill_matrix(C, n)
fill_matrix(D, n)
fill_matrix(E, n)

for i in range(n):
    A.append(E[i] + B[i])
for i in range(n):
    A.append(D[i] + C[i])

print('Матрица E:')
mat_print(E, n)
print('Матрица B:')
mat_print(B, n)
print('Матрица D:')
mat_print(D, n)
print('Матрица C:')
mat_print(C, n)
print('Матрица A:')
mat_print(A, N)

for i in range(1, n - 1):
    if i <= n // 2:
        a = n - i - 1
    else:
        a = i
    for j in range(n - 1, a, -1):
        summ_43 += C[j][i]
print('сумма чисел, по периметру области 3 в матрице С:', summ_43)

for i in range(1, n - 1):
    if i <= n // 2:
        a = n - i - 1
    else:
        a = i
    for j in range(n - 1, a, -1):
        summ_42 += C[i][j]
print('сумма чисел, по периметру области 2 в матрице С:', summ_42)

if summ_43 > summ_42:
    for i in range(1, n - 1):
        if i <= n // 2:
            end_row = n - i - 1
        else:
            end_row = i
        for j in range(n - 1, end_row, -1):
            a = C[j][i]
            C[j][i] = C[i][j]
            C[i][j] = a
    print('Матрица С после изменений:')
    mat_print(C, n)
    for i in range(n):
        F.append(E[i] + B[i])
    for i in range(n):
        F.append(D[i] + C[i])
else:
    for i in range(n):
        F.append(B[i] + E[i])
    for i in range(n):
        F.append(D[i] + C[i])
print('Матрица F:')
mat_print(F, N)

for row in range(0, N):
    Fr = []
    for i in range(0, N):
        sum = 0
        for j in range(0, N):
            sum += F[row][j] * A[j][i]
        Fr.append(sum)
    FA.append(Fr)
print('Результат перемножения матриц F и A: ')
mat_print(FA, N)

for i in range(0, N):
    Fi = []
    for j in range(0, N):
        Fi.append(F[j][i])
    Ft.append(Fi)
print('Транспонированная матрица F: ')
mat_print(Ft, N)

for row in range(N):
    for col in range(N):
        Ft[row][col] = K * Ft[row][col]
print('Транспонированная матрица F умноженная на K: ')
mat_print(Ft, N)

fill_matrix(FinalMat, N)
for row in range(N):
    for col in range(N):
        FinalMat[row][col] = FA[row][col] - Ft[row][col]

print('Получившаяся матрица: ')
mat_print(FinalMat, N)
