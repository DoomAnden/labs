# Натуральные числа. Выводит на экран числа, убирая нечетные цифры в каждом четном по порядку числе.
# Убранные цифры печать отдельно прописью.

buff_len = 1
work_buff = ''
numbers = []
odd = []


def words(n):
    num = {0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
         6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
    return num.get(n)


with open('subbav.txt', 'r') as f:
    buff = f.read(buff_len)
    if not buff:
        print('Файл пуст')
    while buff:
        while '0' <= buff <= '9':
            if '0' <= buff <= '9':
                work_buff += buff
            buff = f.read(buff_len)
        if len(work_buff) > 0:
            numbers.append(work_buff)
            if len(numbers) % 2 == 0:
                n = numbers[-1]
                a = ''
                for i in n:
                    if int(i) % 2 != 0 and i not in odd:
                        odd.append(i)
                    if int(i) % 2 == 0:
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
            a += words(int(i)) + ' '
        print('Убранные нечетные цифры: ' + a)