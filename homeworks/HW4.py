"""
Запросить у пользователя число N - ширина треугольника.

1. Вывести треугольник #1 с шириной N с помощью цикла while
2. Вывести треугольник #2 с шириной N с помощью цикла while

Задание со звездочкой:
3. Вывести треугольник #3 с шириной N с помощью цикла while
4. Вывести треугольник #4 с шириной N с помощью цикла while
"""

# task1
N = int(input('width : '))
i = 1
while i <= N:
    r = N
    while r >= i:
        print("*", end=" ")
        r -= 1
    print()
    i += 1

# task 2

N = int(input('width : '))
i = 1
while i <= N:
    r = 1
    while r <= i:
        print("*", end=" ")
        r += 1
    print()
    i += 1

# task 3
N = int(input('width : '))
i = N
while i >= 1:
    row = N
    while row > i:
        print(' ', end=' ')
        row -= 1
    a = 1
    while a <= i:
        print('*', end=' ')
        a += 1
    print()
    i -= 1


# task 4
N = int(input('width : '))
i = 1
while i <= N:
    row = i
    while row < N:
        # display space
        print(' ', end=' ')
        row += 1
    a = 1
    while a <= i:
        print('*', end=' ')
        a += 1
    print()
    i += 1
