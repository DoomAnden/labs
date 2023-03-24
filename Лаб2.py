# Натуральные числа. Выводит на экран числа, убирая нечетные цифры в каждом четном по порядку числе.
# Убранные цифры печать отдельно прописью.
import re
numbers = []
odd = []


def words(n):
    numeros = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять',
               '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять', 'A': 'A', 'B': 'B',
               'C': 'C', 'D': 'D', 'E': 'E', 'F': 'F'}
    return numeros.get(n)


with open('test.txt', 'r') as f:
    file = f.read()
    if not file:
        print('Файл пуст')
        quit()
    for i in re.findall(r'[13579BDF]', file):
        if words(i) not in odd:
            odd.append(words(i))
    numbers = re.findall(r'[^0 \n]\d+', file)
    for i in range(1, len(numbers), 2):
        a = ''
        u = re.findall(r'[^13579BDF]', numbers[i])
        for j in u:
            a += j
        numbers[i] = a
    if not numbers:
        print('Нет подходящих цифр')
        quit()
    else:
        print('Числа с убранными нечетными цифрами в каждом четном по порядку числе:', *numbers)
        print('Убранные нечетные цифры: ', *odd)