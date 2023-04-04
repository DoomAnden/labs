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
    lines = re.split(r"[' \n]", file)
    if not file:
        print('Файл пуст')
        quit()
    for j in lines:
        if re.fullmatch(r'[1234567890ABCDEF]+', j):
            if len(numbers) % 2 != 0:
                a = ''
                y = re.findall(r"[^24680ACE]", j)
                for i in y:
                    if words(i) not in odd:
                        odd.append(words(i))
                u = re.findall(r"[^13579BDF]", j)
                for i in u:
                    a += i
                numbers.append(a)
            else:
                numbers.append(j)
    if not numbers:
        print('Нет подходящих цифр')
        quit()
    else:
        print('Числа с убранными нечетными цифрами в каждом четном по порядку числе:', *numbers)
        print('Убранные нечетные цифры: ', *odd)