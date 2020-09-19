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
print(a[1][2])

import random

class makecharacter:
    def __init__(self, id):
        self.name = id
        self.hp = random.randrange(475, 900)
        self.mp = random.randrange(430, 600)
        self.p = random.randrange(57, 80)
        self.s = random.randrange(171, 240)
        print("{}가 생성되었습니다.\nhp:{}\nmp:{}\n공격력:{}".format(self.name, self.hp, self.mp, self.p))
    def attack(self):
        return self.p

    def critical(self):
        ran = 2
        self.p * ran
        return self.p

    def attacked(self, atk):
        self.hp = self.hp - atk

    def skill(self):
       self.mp = self.mp - 150
       return self.s



id = input("Enter characer name : ")

ogar = makecharacter(id)

id = input("Enter characer name : ")

mc = makecharacter(id)



while True:
    s = random.randrange(1, 5)
    if s == 3:
        mc.attacked(ogar.skill())
    else:
        c = random.randrange(1, 10)
        if c == 3:
            mc.attacked(ogar.critical())
        else: mc.attacked(ogar.attack())
        if mc.hp <= 0:
            print("{} 사망".format(mc.name))
            break



    print("after mc hp: ", mc.hp)
    print("after ogar mp: ", ogar.mp)
    print("before ogar hp: ", ogar.hp)

    print("before mc mp: ", mc.mp)
    s = random.randrange(1, 5)
    if s == 3:
        ogar.attacked(mc.skill())
    else:
        c = random.randrange(1, 10)
        if c == 3:
            ogar.attacked(mc.critical())
        else:ogar.attacked(mc.attack())
        if ogar.hp <= 0:
            print("{} 사망".format(ogar.name))
            break

    print("after ogar hp: ", ogar.hp)
    print("after mc mp: ", mc.mp)"""

f = open("/Users/scratch1/Desktop/test.txt", "r")

teep = f.readlines()

print(teep)

