# Задание 1: Пользователь вводит слово, если это слово является полиндромом, то вывести '+', иначе '-'

palindrome = str(input('any palindrome: '))
palindrome = palindrome.casefold()
reverse = reversed(palindrome)
if list(palindrome) == list(reverse):
    print('+')
else:
    print('-')

# Задание 2: Пользователь вводит текст и слово которое нужно найти, если это слово есть в тексте, вывести 'YES', иначе 'NO'

text = str(input('enter any text: '))
word = str(input('preferred word: '))
if word in text:
    print('YES')
else:
    print('NO')

# Задание 3:Пользователь вводит строку. Если она начинается на 'abc', то заменить их на 'www', иначе добавить в конец строки 'zzz'.

userstext = str(input('enter any text: '))
updatedtext = userstext.replace('abc', 'www')
endtext = userstext.replace(userstext, 'zzz')
if userstext.startswith('abc'):
    print(updatedtext)
else:
    print(userstext + endtext)

# Задание 4: Пользователь вводит текст, удалить в тексте все цифры и вывести строку пользователю.

usertext = str(input('enter any text: '))
text = ''.join([x for x in usertext if not x.isdigit()])
print(text)

# Задание 5: Написать валидатор для почты. Пользователь вводит почту, а программа должна проверить, что в почте есть символ '@' и '.', и если это так, то вывести "YES", иначе "NO"

enteremail = str(input('Your email: '))
dot = '.'
crh = '@'
if dot in enteremail and crh in enteremail:
    print('YES')
else:
    print('NO')