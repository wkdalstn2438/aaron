"""
while a < 5:
    print("hi", a)
    a = a + 1
"""

"""
a = 2
b = 1
while a < 10:
    b = 1
    while b < 10:
        print("{} x {} = {}".format(a, b, a*b))
        b = b + 1
    a = a + 1
"""
"""
a = []
a.append(3)
a.append(4)
print(a[0])
"""

"""
a = [2, 3, 4,5]

for i in range(len(a)):
    print(a[i])
"""
"""
import random
a = []

for i in range(10):
    b = random.randrange(1, 100)
    a.append(b)

print(a)
c = a[0]
for j in range(10):
    if c < a[j]:
        c = a[j]

print("c", c)
"""
"""while (a % 2):
         a == 0 or a == 1
"""
"""
s = 0
e = 100
m = (s + e)//2
a = int(input())
for i in range(100):
    if a == m:
        break
    elif a > m:
        s = m
    else:
        e = m

    m = (s + e) // 2
if i > 50:
    print("not find value")
else:
    print("find", i)
"""
"""
b = input()
reverse = []
not_reverse = []
for i in range(len(b)):
    reverse.append(b[i])
    not_reverse.append([len(b) -1 - i])

flag = 0
""""""
a = ([1, 2, 3,], [4, 5, 6,])
print(a[1][2])"""
def add_test(x, y):

    return x + y

c = add_test(1, 3)
print(c)