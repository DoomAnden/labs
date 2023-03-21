# Натуральные числа. Выводит на экран числа, убирая нечетные цифры в каждом четном по порядку числе.
# Убранные цифры печать отдельно прописью.
import re
numbers = []
odd = []


def words(n):
    num = {0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
         6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
    return num.get(n)


with open('subbav.txt', 'r') as f:
    file = f.read()
    if not file:
        print('Файл пуст')
        quit()
    o = re.findall(r'[13579]', file)
    for i in o:
        if words(int(i)) not in odd:
            odd.append(words(int(i)))
    u = re.findall(r'\d+', file)
    for i in u:
        numbers.append(i)
        if len(numbers) % 2 == 0:
            a = ''
            for j in i:
                if int(j) % 2 == 0:
                    a += j
            numbers[-1] = a
    if not numbers:
        print('Нет подходящих цифр')
        quit()
    else:
        print('Числа с убранными нечетными цифрами в каждом четном по порядку числе:', *numbers)
        print('Убранные нечетные цифры: ', *odd)
