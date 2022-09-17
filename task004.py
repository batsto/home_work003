# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное. 
# Подумайте, как это можно решить с помощью рекурсии.

# Пример:

# 45 -> 101101
# 3 -> 11
# 2 -> 10


a = int(input())

def dec_to_bin(x):
    result = []
    a = 0
    while (x >= 1):
        if(x%2 == 0):
            a = 0
        else:
            a = 1
        result.append(a)
        x = x//2
    result.reverse()
    return result

print(a)
print(dec_to_bin(a))
