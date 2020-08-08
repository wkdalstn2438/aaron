import math

t = int(input())

for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    maxR = r1 if r1 > r2 else r2
    minR = r2 if r1 > r2 else r1

    result = 0

    # 1. 원이 완전히 겹친 경우
    if distance == 0 and maxR == minR:
        result = -1
    # 2. 원이 내접 또는 외접하는 경우
    elif maxR == minR + distance or maxR + minR == distance:
        result = 1
    # 3. 원이 만나지 않는 경우(완전히 동떨어짐, 내포하는 경우)
    elif maxR + minR < distance or maxR > min + distance:
        result = 0
    # 4. 나머지의 경우는 무조건 교점이 두 개인 경우
    else:
        result = 2

    print(result)