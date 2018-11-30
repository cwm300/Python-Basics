print('Question #1: Is your birthday in Set 1?')
print()
print(' 1  3  5  7')
print(' 9 11 13 15')
print('17 19 21 23')
print('25 27 29 31')
print()
a = input('Enter(n)o or (y)es: ')
if a == 'y':
   A = 1
if a == 'n':
   A = 0
print()
print('Question #2: Is your birthday in Set 2?')
print()
print(' 2  3  6  7')
print('10 11 14 15')
print('18 19 22 23')
print('26 27 30 31')
print()
b = input('Enter(n)o or (y)es: ')
if b == 'y':
   B = 2
if b == 'n':
   B = 0
print()
print('Question #3: Is your birthday in Set 3?')
print()
print(' 4  5  6  7')
print('12 13 14 15')
print('20 21 22 23')
print('28 29 30 31')
print()
c = input('Enter(n)o or (y)es: ')
if c == 'y':
   C = 4
if c == 'n':
   C = 0
print()
print('Question #4: Is your birthday in Set 4?')
print()
print(' 8  9 10 11')
print('12 13 14 15')
print('24 25 26 27')
print('28 29 30 31')
print()
d = input('Enter(n)o or (y)es: ')
if d == 'y':
   D = 8
if d == 'n':
   D = 0
print()
print('Question #5: Is your birthday in Set 5?')
print()
print('16 17 18 19')
print('20 21 22 23')
print('24 25 26 27')
print('28 29 30 31')
print()
e = input('Enter(n)o or (y)es: ')
if e == 'y':
   E = 16
if e == 'n':
   E = 0
print()
x = A + B + C + D + E
print('Your birthday is ', x, '!', sep='')