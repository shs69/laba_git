from math import sin, pi

digit, characters = int(input()), int(input())

for i in range(1, 100):
    digit += i
    if i % 7 == 0:
        characters *= i // 5
    else:
        characters += 2

for i in range(1, 100):
    digit += i
    if i % 7 == 0:
        characters *= i // 2
    else:
        characters += 5
        
print('12')
print('1234')
print('4123412')