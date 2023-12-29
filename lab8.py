from tkinter import *
import random
import copy

'''
Дан одномерный массив. Сформировать все возможные варианты
данного массива, если в массиве сумма модуля отрицательных элементов
будет больше чем сумма положительных перестанавливать отрицательные элементы на четных позициях.
'''

import random
import itertools


class array:
    def __init__(self, n):
        self.arr = [random.randint(-10, 10) for _ in range(n)]

    def print_array(self, array):                # Вывод массива
        if array == []:
            for column in self.arr:
                txt.insert(END, '{:4}'.format(str(column)))
            txt.insert(END, '\n')
        else:
            for column in array:
                txt.insert(END, '{:4}'.format(str(column)))
            txt.insert(END, '\n')
    def iter_combinations(self, indexes):
        count = 0
        for combination in itertools.permutations(indexes):
            replace = self.arr.copy()
            for i in range(len(combination)):
                replace[indexes[i]] = self.arr[combination[i]]
            self.print_array(replace)
            count += 1
        return count

    def F_iter(self):
        indexes = []
        for i in range(len(self.arr)):
            if self.arr[i] < 0:
                indexes.append(i)
        return self.iter_combinations(indexes)

    def F_iter_two(self):
        indexes = []
        sum = 0
        for i in range(len(self.arr)):
            sum += self.arr[i]
            if self.arr[i] < 0 and i % 2 == 1:
                indexes.append(i)
        if sum >= 0:
            txt.insert(END, 'Сумма модуля отрицательных элементов оказалась меньше суммы положительныx:\n', sum)
            txt.insert(END, 'Меняем все отрицательные элементы местами.\n')
            return self.F_iter()
        else:
            txt.insert(END, 'Сумма модуля отрицательных элементов оказалась больше суммы положительных:\n', abs(sum))
            txt.insert(END, 'Меняем отрицательные элементы на четных позициях.\n')
        return self.iter_combinations(indexes)

def button1():
    txt.delete('1.0', END)
    if entr.get():
        try:
            if int(entr.get()) > 0:
                n = array(int(entr.get()))
                n.F_iter_two()
            else:
                txt.insert(END, 'Введенное число отрицательное.')
        except ValueError:
            txt.insert(END, 'Введенное значение не является числом.')
    else:
        txt.insert(END, 'Введите число')



windowEntry = Tk()
windowEntry.title('Lab 8')

button = Button(windowEntry, text='Продолжить', command=button1)
entr = Entry(windowEntry, width=10)
lbl = Label(windowEntry, width=45, text='Размер массива:')
txt = Text(windowEntry, width=100)
scrollbar = Scrollbar(orient="vertical", command=txt.yview)
info = Label(windowEntry, text='Дан одномерный массив. Сформировать все возможные варианты'
                                '\n данного массива, если в массиве сумма модуля отрицательных элементов'
                                '\n будет больше чем сумма положительных перестанавливать отрицательные элементы на четных позициях.')

lbl.place(x=30, y=150)
entr.place(x=100, y=200)
button.place(x=100, y=250)
txt.place(x=0, y=300)
scrollbar.place(x=800, y=300, height=300)
info.place(x=30, y=50)

txt["yscrollcommand"] = scrollbar.set
entr.focus()
windowEntry.geometry('900x600')
windowEntry.mainloop()

