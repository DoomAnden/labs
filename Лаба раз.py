def number_to_words(n):
    f = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
         6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
    return f.get(n)

lines = []
with open('digit.txt') as f:
    file = f.read()
    for i in file.split():
        lines.append(i)
print(lines)

a = lines[1::2]
print(a)
for j in a:
    answer =  str(j) + " - "
    for i in str(j):
        if   i.isdigit() == True and int(i) %2 != 0:
            answer += number_to_words(int(i)) + " "
    print(answer)
