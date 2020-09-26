"""
def add_func(d, e):
    c = d + e
    return c

a = int(input("첫 번째 숫자를 입력해주세요: "))
b = int(input("두 번째 숫자를 입력해주세요: "))

f = add_func(a, b)

print("{} + {} = {}".format(a, b, f))

def aad_fnus(o, p):
    t = o - p
    return t

c = int(input("첫 번째 숫자를 입력해주세요; "))
d = int(input("두 번째 숫자를 입력해주세요: "))

r = aad_fnus(c, d)

print("{} - {} = {}".format(c, d, r))

    q = g * h
    return q
def aaa_fune(g, h):

j = r
k = f

y = aaa_fune(j, k)

print("{} print(line.split('\n')[0])* {} = {}".format(k, j, y))
"""

#f = open("melon.text", 'r')
#lines = f.readlines()

#i#d = input("id : ")
#pwd = input("pwd : ")

#flag = 0
#for line in lines:
    #server_id = line.split(',')[0]
    #server_pwd =
    #if server_pwd == pwd and server_id == id:
        #print("로그인이 되었습니다.")
        #flag = 1
        #break

#if flag == 0:
    #print("로그인에 실패했습니다.")
f = open("melon.text", 'a')
fr = open("melon.text", 'r')

lines = fr.readlines()
for line in lines:
    server_id = line.split(',')[0]
    server_pwd = line.split(',')[1]
    for

id = input()
pw = input()

f.write(id + "," + pw + '\n')