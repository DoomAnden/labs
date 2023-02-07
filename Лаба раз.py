def number_to_words(n):
    f = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
         6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
    return f.get(n)

from random import randint

numbers = []
for i in range(20):
    numbers.append(randint(1, 20))
print(numbers)
a = numbers[1::2]
print(a)
for j in a:
    answer =  str(j) + " - "
    for i in str(j):
        if int(i) %2 != 0:
            answer += number_to_words(int(i)) + " "
    print(answer)