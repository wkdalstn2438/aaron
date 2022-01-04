import random
a = []
c = 0
d = 0

for i in range(10):
    a.append(random.randrange(1, 21))
    a.append(int(input()))

while c == c:
    for i in range(len(a)-1):
        if a[i] <= a[i + 1]:
            c = c + 1
    if c == len(a)-1:
        break
    else:
        c = 0
    for i in range(len(a)-1):
        if a[i] > a[i + 1]:
            d = a[i + 1]
            a[i + 1] = a[i]
            a[i] = d
print(a)