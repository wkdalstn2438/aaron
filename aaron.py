"""
f = open("aron.txt","r")
lines = f.readlines()

for line in lines:
    print(line)

for line in lines:
    print(line.split('\n')[0])

a = "hihihikbyebye"
b = a.split('k')
print(b)

def a1():
    id = input("id:")
    pwd = input("pwd:")
    for line in lines:
        server_id = line.split(',')[0]
        server_pwd = line.split(',')[1].split('\n')[0]
        if id == server_id and pwd == server_pwd:
            print("로그인 완료")
            return
    print("다시")

def a2():
    id = input("id:")
    pwd = input("pwd:")
    flag = 0
    for line in lines:
        server_id = line.split(',')[0]
        server_pwd = line.split(',')[1].split('\n')[0]
        if id == server_id and pwd == server_pwd:
            print("로그인 완료")
            return
    fr.write(id + ',' + pwd + '\n')
    print("가입완료")

f = open("test.txt","a")
fr = open("test.txt","r")
id = input("아이디를 입력하세요:")
pwd = input("비밀번호를 입력하세요:")
for line in lines:
    server_id = line.split(',')[0]
    server_pwd = line.split(',')[1].split('\n')[0]
    if id == server_id:
        print("이미 가입되어 있습니다.")
    exit()
f.write(id + ',' + pwd + '\n')
print("가입완료")
def make_board():

    a =[]
    for i in range(9):
        a.append("-")

    return a\
"""

def make_board():

    a =[]
    for i in range(9):
        a.append("-")

    return a

def see_board():
    print(board[0] + "|"+ board[1] + "|" + board[2])
    print("ㅡㅡㅡ")
    print(board[3] + "|"+ board[4] + "|" + board[5])
    print("ㅡㅡㅡ")
    print(board[6] + "|"+ board[7] + "|" + board[8])


board = make_board()
see_board()
player1 = input("O or X")
if player1 == "O":
    player2 = "X"
    print("player1은 O, player2은 X")
else:
    player2 = "O"
    print("player1은 X, player2은 O")

for i in range(9):

    select_turn = int(input("1.[1] 2.[2] 3.[3] 4.[4] 5.[5] 6.[6] 7.[7] 8.[8] 9.[9]"))

    if board[select_turn - 1] == '-':
        board[select_turn - 1] = player1
    see_board()
    print("player1이 {}에 {}을 표시했습니다.".format(select_turn, player1))


    select_turn = int(input("1.[1] 2.[2] 3.[3] 4.[4] 5.[5] 6.[6] 7.[7] 8.[8] 9.[9]"))
    if board[select_turn - 1] == '-':
        board[select_turn - 1] = player2
    see_board()
    print("player2이 {}에 {}을 표시했습니다.".format(select_turn, player2))

    select_turn = int(input("1.[1] 2.[2] 3.[3] 4.[4] 5.[5] 6.[6] 7.[7] 8.[8] 9.[9]"))

    if board[select_turn - 1] == '-':
        board[select_turn - 1] = player1
    see_board()
    print("player1이 {}에 {}을 표시했습니다.".format(select_turn, player1))


    select_turn = int(input("1.[1] 2.[2] 3.[3] 4.[4] 5.[5] 6.[6] 7.[7] 8.[8] 9.[9]"))
    if board[select_turn - 1] == '-':
        board[select_turn - 1] = player2
    see_board()
    print("player2이 {}에 {}을 표시했습니다.".format(select_turn, player2))
    select_turn = int(input("1.[1] 2.[2] 3.[3] 4.[4] 5.[5] 6.[6] 7.[7] 8.[8] 9.[9]"))

    if board[select_turn - 1] == '-':
        board[select_turn - 1] = player1
    see_board()
    print("player1이 {}에 {}을 표시했습니다.".format(select_turn, player1))


    select_turn = int(input("1.[1] 2.[2] 3.[3] 4.[4] 5.[5] 6.[6] 7.[7] 8.[8] 9.[9]"))
    if board[select_turn - 1] == '-':
        board[select_turn - 1] = player2
    see_board()
    print("player2이 {}에 {}을 표시했습니다.".format(select_turn, player2))
    select_turn = int(input("1.[1] 2.[2] 3.[3] 4.[4] 5.[5] 6.[6] 7.[7] 8.[8] 9.[9]"))

    if board[select_turn - 1] == '-':
        board[select_turn - 1] = player1
    see_board()
    print("player1이 {}에 {}을 표시했습니다.".format(select_turn, player1))


    select_turn = int(input("1.[1] 2.[2] 3.[3] 4.[4] 5.[5] 6.[6] 7.[7] 8.[8] 9.[9]"))
    if board[select_turn - 1] == '-':
        board[select_turn - 1] = player2
    see_board()
    print("player2이 {}에 {}을 표시했습니다.".format(select_turn, player2))
    select_turn = int(input("1.[1] 2.[2] 3.[3] 4.[4] 5.[5] 6.[6] 7.[7] 8.[8] 9.[9]"))

    if board[select_turn - 1] == '-':
        board[select_turn - 1] = player1
    see_board()
    print("player1이 {}에 {}을 표시했습니다.".format(select_turn, player1))
    break
