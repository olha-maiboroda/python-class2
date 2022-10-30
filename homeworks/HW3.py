"""
HW3:
1. Пользователь вводит с клавиатуры три числа в переменные a, b, c. Если все числа больше 10 и первые два числа делятся на 3, то вывести yes, иначе no
2. Пользователь вводит с клавиатуры три числа в переменные a, b, c. Найдите наибольшее число из них и запишите в переменную max.
3. Пользователь вводит два числа A и B, нужно вывести сумму всех четных чисел в диапазоне от A до B.
"""

# task 1
a = int(input('Enter number A: '))
b = int(input('Enter number B: '))
c = int(input('Enter number C: '))
if a > 10 and b > 10 and c > 10:
    if not a % 3 and not b % 3:
        print('yes')
else:
    print('no')


# task 2
a = int(input('Enter number A: '))
b = int(input('Enter number B: '))
c = int(input('Enter number C: '))

numbers = [a, b, c]
max_number = numbers[0]

for number in numbers:
    if number > max_number:
        max_number = number
print(max_number)



# task 3
a = int(input('Enter number A: '))
b = int(input('Enter number B: '))
summa = 0

for i in range(a, b):
    if i % 2 == 0:
        summa = summa + i
print(summa)



