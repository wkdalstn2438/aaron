"""
for a in range(10):
    print((10-a)*"*")

for a in range(100):
    if one % 3 == 0 and one != 0:
        print("*")
    else:
        print(a)

for a in range(100):
    if one_condition and ten_condition:
        print("**")
    elif one_condition or ten_condition:
        print("*")
    else:
        print(a)

    ten = a // 10
    one = a % 10
    ten_condition = ten % 3 == 0
    one_condition = one % 3 == 0

for a in range(2,10):
    for b in range(1,10):
        print(a*b)
for a in range(2,10):
    for b in range(1,10):
        print("{}*{}={}".format(a,b,a*b))
"""
a = int(input())

flag = 0 #1 is prlea

for a in range(2,a):
    if a % 1 == 0:
        flag = 1
        break
if flag == 0:
    print("소수")
else:
    print("소수아님")