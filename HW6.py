# Задание 1: Запросить у пользователя 5 чисел и записать их в список

A = []
print('PLEASE ENTER 5 NUMBERS')
for i in range(5):
    values = int(input(f'Your {i + 1} number: '))
    A.append(values)
print('YOUR ENTERED NUMBERS ARE: ')
print(A)

# Задание 2: Дан список A = [1, 2, 3, 4, 5], Удалить последнее число из списка

A = [1, 2, 3, 4, 5]
del(A[4])
print(A)

# Задание 3: Запросить у пользователя 10 чисел и записать их в список A, запросить у пользователя число N, вывести пользователю сколько в списке A повторяется число N

A = []
for i in range(10):
    numbers = int(input('Enter 10 numbers: '))
    A.append(numbers)
print('Your entered numbers are: ')
print(A)
N = int(input('Enter random number: '))
print(N)
amount = A.count(N)
print(amount)

# Задание 4: Запросить у пользователя число N, Запросить у пользователя N чисел и записать их в список A, Вывести список в обратной последовательности

N = int(input('Enter any number: '))
print(N)
A = []
for i in range(N):
    numbers = int(input('Enter your numbers: '))
    A.append(numbers)
print('Your entered numbers are: ')
print(A)
print('Your reversed numbers are: ')
A.reverse()
print(A)

#Задание 5: Запросить у пользователя 5 чисел и записать их в список A, Записать все числа из списка A которые больше 5 в список C

A = []
C = []
print('PLEASE ENTER 5 NUMBERS')
for i in range(5):
    values = int(input(f'Your {i + 1} number: '))
    A.append(values)
print('YOUR ENTERED NUMBERS ARE: ')
print(f'A = {A}')
for i in A:
    if i > 5:
        C.append(i)
print(f'C = {C}')

#Задание 6: Запросить у пользователя число N, запросить у пользователя N целых чисел и записать их в список A, найти в нем минимальное и максимальное число с помощью цикла (запрещено использовать функцию min, max, sorted, sort). Вывести эти числа.

A = []
N = int(input('Enter any number: '))
for i in range(N):
    number = int(input(f'Your {i + 1} number: '))
    A.append(number)
print('Your entered numbers are: ')
print(A)
max = A[0]
for currentItem in A:
    if currentItem > max:
        max = currentItem
print(f'Max value = {max}')

min = A[0]
for currentItem in A:
    if currentItem < min:
        min = currentItem
print(f'Min value = {min}')


# Задание 7: Пользователь вводит текст, нужно вывести количество чисел в этом тексте, Пример: > 'Lorem 222 ipsum, 1234 dolor 1 sit amet; Количество чисел: 3

anytext = input('Enter any text: ')
print(anytext)
count = 0
for word in anytext.split():
    if word.isdigit():
        count = count + 1
print(count)