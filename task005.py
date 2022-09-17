# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13,








a = int(input())

def create_finnabochi(n):
    if n in (1, 2):
        return 1
    elif n == 0:
        return 0
    return create_finnabochi(n-1) + create_finnabochi(n-2)
        
def list_finnabochi(a):
    result = []
    end_result =[]
    n = 0
    for i in range(0, a):
        n = create_finnabochi(i)
        result.append(n)
    for i in result:
        i *= -1
        end_result.append(i)
    return end_result[::-1] + result


print(list_finnabochi(a))