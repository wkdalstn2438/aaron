# <변수>
# 자료형 = 어떤 종류의 값을 담을 수 있는가
# 123 정수형 값 = int형 a = 1
#
# "abc" 'ㄱㄴㄷ' = str형(string)
#
# 3.14 = float형
#
#
# + - * / % //는 소수점 제거

# input() 어떤것이든 str형로 저장된다

# bool은 ture 와 false 밖에 없다
# ture와 false도 값이다



# <조건부>
# if 조건:
#     실행문

# >, <, ==,!=, <=, >=  ==는 같다면 이다
# or 는 둘중 하나만 만 되도 작동한다, and는 모두참이어야한다 ()는 우선 순위를 나누어 준다.

# elif는 if 가 성립되면은 무시된다  else는 모두 안될 경우에 성립된다


# <반복문>

# for i in range(반복횟수):

# 그 수가 짝수인지 홀수인지 구분한다
# a = int(input())
#
# if a % 2 == 1:
#     print("odd")
#
# if a == 0:
#     print("0")
#
# elif a % 2 == 0:
#     print("even")

# 별만들기
# for i in range(1,11):
#     print("*"*i)

# for i in range(1,11):
#     print("*"*(11-i))

# 그 수가 소수인지 아닌지 알아보는 코드

# a = int(input())
# x = 0
#
# for i in range(1, a + 1):
#     if a % i == 0:
#         x = x + 1
#
# if x > 2:
#     print("소수 아님")
# elif x < 2:
#     print("소수 아님")
# else:
#     print("소수")

# import
# import란 다른 파일에 있는 함수코드를 사용하겠다고 선언해주는 함수

# import random
#
# a = random.randrange(100)
#
# print(a)
# print(random.randrange(100))

# list
# 리스트 이름 = []


# a = []
# a.append(100)
# print(a)
# a.append(101)
# print(a)
# a[0] = 102
# print(a)


# a = [45,141,11]
# print(len(a))# 리스트의 길이를 알려주는 함수
# a = [6,3,8,1,4]
# print(a[0])


# while (조건):
#     반복할 코드

# a = [7,1,3,5,4]
# c = 0
#
# while c == c:
#     for z in range(4):
#         if a[z] <= a[z + 1]:
#             c = c + 1
#     if c == 4:
#         break
#     else:
#         c = 0
#
#     for i in range(4):
#         if a[i] > a[i + 1]:
#             b = a[i]
#             a[i] = a[i + 1]
#             a[i + 1] = b
# print(a)

# map은 여러 데이터를 변환한다.