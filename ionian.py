import random

a = []
mn = 0


for i in range(10):
    a.append(random.randrange(10))

mn = a[0]
b = 0
c = 0

print(a)

for z in range(len(a)-1):
    mn = a[z]
    for i in range(z, len(a)):
        if mn > a[i]:
            mn = a[i]
            b = i

    c = a[z]
    a[z] = a[b]
    a[b] = c
print(a)