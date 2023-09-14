from math import sin, pi

for i in range(1, 100):
    digit += i
    if i % 7 == 0:
        characters *= i // 2
    else:
        characters += 5

digit, characters = int(input()), int(input())

print('12')
print('1234')
print('4123412')

for i in range(1, 100):
    digit += i
    if i % 7 == 0:
        characters *= i // 5
    else:
        characters += 2


        



