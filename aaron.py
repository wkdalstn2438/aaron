# a = list(map(int, input().split(" ")))
import random

v = int(input())
a = []
b = 0

for i in range(v):
    a.append(random.randrange(50))
print(a)
while True:
    if b == len(a)-1:
        break
    b = 0
    for i in range(len(a)-1):
        if a[i] <= a[i + 1]:
            b = b + 1
    for i in range(len(a)-1):
        if a[i] > a[i + 1]:
            c = a[i + 1]
            a[i + 1] = a[i]
            a[i] = c
print(a)