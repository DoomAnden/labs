'''
1. Дан одномерный массив. Сформировать все возможные варианты
данного массива путем перестановки отрицательных элементов

2. Дан одномерный массив. Сформировать все возможные варианты
данного массива, если в массиве сумма модуля отрицательных элементов
будет больше чем сумма положительных перестанавливать отрицательные элементы на четных позициях.
'''

import random
import itertools


class array:
    def __init__(self):
        n = self.accept_number('Введите размерность массива: ')
        self.arr = [random.randint(-10, 10) for _ in range(n)]

    def print_array(self, array):                # Вывод массива
        if array == []:
            for column in self.arr:
                print('{:4}'.format(column), end=' ')
            print()
        else:
            for column in array:
                print('{:4}'.format(column), end=' ')
            print()

    def accept_number(self, description):  # Проверка положительное ли число было введено
        while True:
            try:
                k = int(input(description))
                if k > 0:
                    return k
                else:
                    print('Введенное число отрицательное.')

            except ValueError:
                print('Введенное значение не является числом.')

    def iter_combinations(self, indexes):            # Перебор всех возможных комбинаций
        count = 0
        for combination in itertools.permutations(indexes):
            replace = self.arr.copy()
            for i in range(len(combination)):
                replace[indexes[i]] = self.arr[combination[i]]
            self.print_array(replace)
            count += 1
        return count

    def F_iter(self):           # Итеративное решение 1 задачи
        indexes = []
        for i in range(len(self.arr)):
            if self.arr[i] < 0:
                indexes.append(i)
        return self.iter_combinations(indexes)

    def F_iter_two(self):           # Итеративное решение 2 задачи
        indexes = []
        sum = 0
        for i in range(len(self.arr)):
            sum += self.arr[i]
            if self.arr[i] < 0 and i % 2 == 1:
                indexes.append(i)
        if sum >= 0:
            print('Сумма модуля отрицательных элементов оказалась меньше суммы положительныx:', sum)
            print('Меняем все отрицательные элементы местами.')
            return self.F_iter()
        else:
            print('Сумма модуля отрицательных элементов оказалась больше суммы положительных:', abs(sum))
            print('Меняем отрицательные элементы на четных позициях.')
        return self.iter_combinations(indexes)

n = array()
print('Начальный массив:')
n.print_array([])
print('Итеративный перебор возможных вариантов.')
print('Общее количество вариантов: ', n.F_iter_two())
