"""
def gc(a, b):
    for i in range(1, a + 1):
        if a % i == 0 and b % i == 0:
            af = i
    print(af)
    if af == 1:
        print("서로소")
    elif af != 1:
        print("서로소 아님")


def gcd(a, b):
    for i in range(1, a + 1):
        if a % i == 0 and b % i == 0:
            af = i
    return af

a = int(input())
b = int(input())
gc(a, b)
gcd(a,b)
"""
"""
a = input("입력:")
if a[7] == '3' or a[7] == '1':
    print("성별:남자")
else:
    print("성별:여자")
if a[7] == '1' or a[7] == '2':
    print("나이:{}".format(2020 - (1900 + 10 * int(a[0]) + int(a[1]))))
else:
    print("나이:{}".format(2020 - (2000 + 10 * int(a[0]) + int(a[1]))))
"""
"""
def pepole(a):
    if(len(a)!=14):
        print("잘못 입력하셨습니다.")
        exit()
    else:
        if a[7] == '3' or a[7] == '1':
            gen = '남자'
        else:
            gen = '여자'
        if a[7] == '1' or a[7] == '2':
            age = 2020 - (1900 + 10 * int(a[0]) + int(a[1])) + 1
        else:
            age = 2020 - (2000 + 10 * int(a[0]) + int(a[1])) + 1
    print("나이는 {}살 성별은 {}입니다".format(age, gen))
a = input()
pepole(a)
"""
"""제기함수
def fact(a):
    if a <= 0:
        return 1
    else:
        return a * fact(a-1)

a = int(input())
print("{}".format(fact(a)))
"""
class B:
    def say(self):#매소드
        print("안녕")
class A:
    def __init__(self, name):
        self.name = name
    def say(self):#매소드
        print("안녕{}".format(self.name))

b = input()
a1 = A(b) #객체
a1.say()

a2 = B()
a2.say()
