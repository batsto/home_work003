# 2-Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]



from random import randint


array = [randint(0,10) for item in range(0,10)]


def sum_pairs_numbers(a:list):
    result = []
    x = 0
    item =0
    while x < (len(a)/2 if len(a)%2 == 0 else len(a)//2 + 1):
        item = a[x] + a[len(a)-1-x]
        result.append(item)
        x += 1
        
    return result

print(array)
print(sum_pairs_numbers(array))





