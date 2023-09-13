from math import sin, pi

digit, characters = int(input()), int(input())

for i in range(1, 100):
    digit += i
    if i % 7 == 0:
        characters *= i // 5
    else:
        characters += 2
    
def func(x):
    return sin(x)

print(func(pi/2))