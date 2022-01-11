# import random
#
# a = []
# b = 0
# c = 0
#
# for i in range(10):
#     a.append(random.randrange(1, 100))
#
# while b == b:
#     for i in range(len(a)-1):
#         if a[i] <= a[i + 1] :
#             b = b + 1
#     if b == len(a)-1:
#         break
#     b = 0
#     for i in range(len(a)-1):
#         if a[i] > a[i + 1]:
#             c = a[i + 1]
#             a[i + 1] = a[i]
#             a[i] = c
# print(a)
# print(a[0], a[9])

import random

a = []
mx = 0
mn = 0

for i in range(10):
    a.append(random.randrange(1, 100))

mx = a[0]
mn = a[0]

for i in range(len(a)):
    if mx < a[i]:
        mx = a[i]
    if mn > a[i]:
        mn = a[i]
print(a)
print(mn, mx)