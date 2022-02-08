# class Fourcal:
#     def __init__(self):
#         self.result = 0
#
#     def add(self, num):
#         self.result += num
#         return self.result
# a = Fourcal()
# print(a.add(10))
# b = Fourcal()
# print(b.add(21))

# class Fourcal:
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second
#
#     def add(self):
#         result = self.first + self.second
#         return result
#
#     def sub(self):
#         result = self.first - self.second
#         return result
#
#     def mul(self):
#         result = self.first * self.second
#         return result
#
#     def div(self):
#         result = self.first / self.second
#         return result
#
# class MoreFourcal(Fourcal):
#     def pow(self):
#         result = self.first ** self.second
#         return result
#
# a = MoreFourcal(3, 4)
# print(a.add())
# print(a.sub())
# print(a.mul())
# print(a.div())
# print(a.pow())

# def print_reverse(a):
#     print(a[::-1])

# def print_score(a):
#     b = 0
#     for i in a:
#         b += i
#     return b / len(a)
# print(print_score([1,2,3]))

# def print_score(a):
#     print(sum(a)/len(a))
# print_score([1,2,3])

# def print_even(a):
#     for i in a:
#         if i % 2 == 0:
#             print(i)

# def print_keys(a):
#     for i in a.keys():
#         print(i)

# def cms(a):
#     print (int(a / 12))
# cms(12000000)

# def make_url(a):
#     print("www."+a+".com")
# make_url("nAver")

# def convert_int(a):
#     return int(a.replace(",", ""))
#
# print(convert_int("1,234,567"))