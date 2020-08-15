"""
a = 0
while a < 5:
    print("hi", a)

a = 2
b = 1
while a < 10:
    print( )
    b = 1
    while b < 10:
        print("{} x {} ={}".format(a, b, a * b))
        b = b + 1
    a = a + 1
a = []
a.append(3)
a.append(4)
a.append(5)
print(a)
print(a[0])

a = []
a.append(3)
a.append(4)
a.append(5)
for i in range(len(a)):
    print(a[i])
a = random.randrange(1,10)
b = []
b.append(a)
print(b)

import random
a = random.randrange(1, 10)
b = []

for i in range(1, 11):
    a = random.randrange(1, 10)
    b.append(a)
for i in range(len(b)):
    print(b[i])
c =b[0]
print(b)
for i in range(1, 10):
    if (c < (b[i])):
        c = b[i]
    elif (c > (b[i])):
        c = c
print(c)
"""
a = int(input())