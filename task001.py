# 1- Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


from operator import index
from random import randint


list1 = [randint(0,10) for i in range(0,11)]

def sum_odd(a:list):
    result = 0
    ind = 0
    for i in a:
        if ind % 2 == 1:
            result  += i
        ind +=1
    return result

print(sum_odd(list1))
print(list1)

