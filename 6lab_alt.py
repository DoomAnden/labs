'''
1. Дан одномерный массив. Сформировать все возможные варианты
данного массива путем перестановки отрицательных элементов

2. Дан одномерный массив. Сформировать все возможные варианты
данного массива, если в массиве сумма модуля отрицательных элементов
будет больше чем сумма положительных перестанавливать отрицательные элементы на четных позициях.
'''

import random
import itertools

def accept_number(description):                    # Проверка положительное ли число было введено
    while True:
        try:
            k = int(input(description))
            if k > 0:
                return k
            else:
                print('Введенное число отрицательное.')

        except ValueError:
            print('Введенное значение не является числом.')

def print_array(array):                # Вывод массива
    for column in array:
        print('{:4}'.format(column), end=' ')
    print()
def iter_combinations(array, indexes):            # Перебор всех возможных комбинаций
    count = 0
    for combination in itertools.permutations(indexes):
        replace = array.copy()
        for i in range(len(combination)):
            replace[indexes[i]] = array[combination[i]]
        print_array(replace)
        count += 1
    return count

def F_iter(array):           # Итеративное решение 1 задачи
    indexes = []
    for i in range (len(array)):
        if array[i] < 0:
            indexes.append(i)
    return iter_combinations(array, indexes)

def F_iter_two(array):           # Итеративное решение 2 задачи
    indexes = []
    sum = 0
    for i in range (len(array)):
        sum += array[i]
        if array[i] < 0 and i % 2 == 1:
            indexes.append(i)
    if sum >= 0:
        print('Сумма модуля отрицательных элементов оказалась меньше суммы положительныx:', sum)
        print('Меняем все отрицательные элементы местами.')
        return F_iter(array)
    else:
        print('Сумма модуля отрицательных элементов оказалась больше суммы положительных:', abs(sum))
        print('Меняем отрицательные элементы на четных позициях.')
    return iter_combinations(array, indexes)

n = accept_number ('Введите размерность массива: ')
array = [random.randint(-10, 10) for i in range(n)]
print('Начальный массив:')
print_array(array)
print('Итеративный перебор возможных вариантов.')
#count = F_iter(array)                 # Для 1 задачи
count = F_iter_two(array)              # Для 2 задачи
print('Общее количество вариантов: ', count)
