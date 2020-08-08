def phytagooras(a, b, c):
    if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
        return True
    else:
        return False

while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break

    print('right' if phytagooras(a, b, c) else 'wrong')