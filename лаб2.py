# Натуральные числа. Выводит на экран числа, убирая нечетные цифры в каждом четном по порядку числе.
# Убранные цифры печать отдельно прописью.
buff_len = 1
work_buff = ''
numbers = []
odd = []
skip = 0


def words(n):
    numbers = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять',
               '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять', 'A': 'A', 'B': 'B',
               'C': 'C', 'D': 'D', 'E': 'E', 'F': 'F'}
    return numbers.get(n)


with open('test.txt', 'r') as f:
    buff = f.read(buff_len)
    if not buff:
        print('Файл пуст')
    while buff:
        if buff == '.':
            skip = 2
        if buff == '-':
            skip = 1
        while buff in ['0', '1', '2', '3', '4', '5', '6', '7',
                       '8', '9', 'A', 'B', 'C', 'D', 'E',
                       'F', '.', '-']:
            work_buff += buff
            buff = f.read(buff_len)
        if len(work_buff) > 0:
            if '-' in work_buff or '.' in work_buff:
                work_buff = ''
                buff = f.read(buff_len)
                continue
            numbers.append(work_buff)
            if len(numbers) % 2 == 0:
                n = numbers[-1]
                a = ''
                for i in n:
                    if i not in ['B', 'D', 'F', 'A', 'C', 'E']:
                        if int(i) % 2 != 0 and i not in odd:
                            odd.append(i)
                        if int(i) % 2 == 0:
                            a += i
                    else:
                        if (i in ['B', 'D', 'F']) and i not in odd:
                            odd.append(i)
                        if i in ['A', 'C', 'E']:
                            a += i
                numbers[-1] = a
        work_buff = ''
        buff = f.read(buff_len)
    if not numbers:
        print('Нет подходящих числа')
    else:
        print('Числа с убранными нечетными цифрами в каждом четном по порядку числе:', *numbers)
        a = ''
        for i in odd:
            a += words(i) + ' '
        print('Убранные нечетные цифры: ' + a)