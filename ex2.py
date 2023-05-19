'''Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)
'''
from random import randint
a = [randint(-10,11) for i in range(5,20)]
print(f"заданный массив: {a}")
b=randint(-10,2)
c=randint(2,11)
index = []
for i in range(0,len(a)):
    if a[i]>=b and a[i]<=c:
        index.append(i)
print(f"индексы элементов, входящих в диапозон {b} - {c} :{index}")
