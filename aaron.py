"""
a = open("aaron.txt", 'r')

totel_linse = a.readlines()

print(totel_linse)

id = input("Enter the id: ")
pad = input("Enter the pad: ")

for line in totel_linse:
    print(line)

"""
#0 1 2
#3 4 5
#6 7


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
    select_turn = int(input("1.[1] 2.[2] 3.[3] 4.[4] 5.[5] 6.[6] 7.[7] 8.[8] 9.[9]"))
    if board[select_turn - 1] == '-':
        board[select_turn - 1] = player2
    see_board()