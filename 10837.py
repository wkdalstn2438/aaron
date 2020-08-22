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
b = [(]

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

a = [1, 2, 3, 4, 5, 6, 7]

print(a[2:5])
"""
"""
b = []
a = int(input())

while (a != 0):
    b.append(a % 2)
    a = a // 2
for i in range(len(b)-1, -1, -1):
    print(b[i])
    while(d):
    e.append(d % 2)
    d = d // 2

a = int(input())
b = 1
c = 100
d = 2
e = 50
while(a < c // d):
    d = d * 2
"""