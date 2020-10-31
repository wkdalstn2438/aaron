"""
f = open("aaea.txt","a")
fr = open("aaea.txt","r")
lines = fr.readlines()

def aar():
    id = input("id:")
    pwd = input("pwd:")
    for line in lines:
        server_id = line.split(',')[0]
        server_pwd = line.split(',')[1].split('\n')[0]
        if id == server_id and pwd == server_pwd:
            print("로그인 완료")
            print("{}님 환영합니다.".format(server_id))
            return
    print("다시")
    aar()
def sc():
    id = input("아이디를 입력하세요:")
    pwd = input("비밀번호를 입력하세요:")
    for line in lines:
        server_id = line.split(',')[0]
        server_pwd = line.split(',')[1].split('\n')[0]
        if id == server_id:
            print("이미 가입되어 있습니다.")
            aar()
    f.write(id + ',' + pwd + '\n')
    print("가입완료")


a = int(input("1[회원가입], 2[로그인]"))
if a == 1:
    sc()
else:
    aar()



def make_board():
    a =[]
    for i in range(9):
        a.append("-")
    return a

def ch_board():
    if board[0] == board[1] and board[1] == board[2] and board[1] != "-":
        return True
    elif board[3] == board[4] and board[4] == board[5] and board[4] != "-":
        return True
    elif board[6] == board[7] and board[7] == board[8] and board[7] != "-":
        return True
    elif board[0] == board[3] and board[3] == board[6] and board[3] != "-":
        return True
    elif board[1] == board[4] and board[4] == board[7] and board[4] != "-":
        return True
    elif board[2] == board[5] and board[5] == board[8] and board[5] != "-":
        return True
    elif board[0] == board[4] and board[4] == board[8] and board[4] != "-":
        return True
    elif board[2] == board[4] and board[4] == board[6] and board[4] != "-":
        return True
    else:
        return False

def ch_d():
    for i in range(0,9):
        if board[i] != "-":
            continue
        else:
            return
    print("무승부")
    exit()

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
player1 = input("O or X").upper()
if player1 == "O":
    player2 = "X"
    print("player1은 O, player2은 X")
else:
    player2 = "O"
    print("player1은 X, player2은 O")

def play_set1():
    select_turn = int(input("1.[1] 2.[2] 3.[3] 4.[4] 5.[5] 6.[6] 7.[7] 8.[8] 9.[9]"))

    if board[select_turn - 1] == '-':
        board[select_turn - 1] = player1
        print("player1이 {}에 {}을 표시했습니다.".format(select_turn, player1))
    else:
        print("다시")
        play_set1()
    see_board()

def play_set2():
    select_turn = int(input("1.[1] 2.[2] 3.[3] 4.[4] 5.[5] 6.[6] 7.[7] 8.[8] 9.[9]"))

    if board[select_turn - 1] == '-':
        board[select_turn - 1] = player2
        print("player1이 {}에 {}을 표시했습니다.".format(select_turn, player1))
    else:
        print("다시")
        play_set2()
    see_board()

for i in range(9):
    play_set1()
    c = ch_board()
    if c:
        print("player1 승리")
        break
    ch_d()

    play_set2()
    c = ch_board()
    if c:
        print("player2 승리")
        break
    ch_d()
"""
"""
def push(stack, a):

    if len(stack) >= max_v:
        print("overflow")
    else:
        stack.append(a)

    return stack

def pop(stack):
    if len(stack) == 0:
        print("underflow")
    else:
        print(stack[len(stack) - 1])
        del stack[len(stack) - 1]

    return stack

max_v = 5
stack = []
while True:

    check = int(input("1 is push, 2 is pop, 3 is exit"))

    if check == 1:
        a = int(input("enter the value : "))
        stack = push(stack, a)
    elif check == 2:
        stack = pop(stack)
    elif check == 3:
        break
"""
a = [3, 5, 1, 2, 7]

for i in range(len(a)):
    for i in range(len(a) - 1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1],a[i]

print(a)