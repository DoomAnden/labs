'''
1. Дан одномерный массив. Сформировать все возможные варианты
данного массива путем перестановки отрицательных элементов

2. Дан одномерный массив. Сформировать все возможные варианты
данного массива, причем сумма первого и последнего отрицательного элементов должна быть максимальной.
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
def iter_combinations(array, indexes, min=0):            # Перебор всех возможных комбинаций
    count = 0
    for combination in itertools.permutations(indexes):
        replace = array.copy()
        for i in range(len(combination)):
            replace[indexes[i]] = array[combination[i]]

        if replace[indexes[0]] + replace[indexes[len(indexes) - 1]] == min:
            print_array(replace)
            count += 1
    return count


def F_iter_two(array):           # Итеративное решение 2 задачи
    indexes = []
    min1, min2 = 0, 0
    for i in range (len(array)):
        if array[i] < 0:
            indexes.append(i)
            if array[i] < min1:
                min2=min1
                min1 = array[i]
            elif array[i] < min2:
                min2 = array[i]
            ma = min1 + min2
    return iter_combinations(array, indexes, ma)

n = accept_number ('Введите размерность массива: ')
array = [random.randint(-10, 10) for i in range(n)]
print('Начальный массив:')
print_array(array)
print('Итеративный перебор возможных вариантов.')
count = F_iter_two(array)              # Для 2 задачи
print('Общее количество вариантов: ', count)
