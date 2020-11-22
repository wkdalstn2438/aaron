"""

a = [15, 11, 1, 3, 8]

for i in range(len(a)):
    for j in range(len(a) - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)

import random
a = []
for i in range(10):
    a.append(random.randrange(1, 200))
print(a)

for i in range(len(a)-1):
    mini = i

    for i in range(i + 1, len(a)):
        if


import pygame

pygame.init()

def car(carImg, x, y):
    gameDisplay.blit(carImg, (x, y))

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('race')

black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()
carImg = pygame.image.load('car (2).jpg')

car_height = 150
car_width = 150
def game_loop():
    x = (display_width * 0.4)
    y = (display_height * 0.7)
    x_change = 0
    y_change = 0
    crashed = False

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_DOWN:
                    y_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                x_change = 0
                y_change = 0
    x += x_change
    y += y_change
    gameDisplay.fill(white)
    car(carImg, x, y)
    if (x > display_width - car_width or x < 0) or (y > display_height - car_height or y < 0):
        crashed = True

    pygame.display.update()
    clock.tick(60)
game_loop()
"""
def cd(a, b, limit):
    data = []
    for x in range(1, limit + 1):
        if x % a == 0 and x % b == 0:
            data.append(x)
    return data

a = int(input("첫번째 숫자를 입력해주세요: "))
b = int(input("두번재 숫자를 입력해주세요: "))
c = int(input("범위 입력: "))

res = cd(a, b, c)
print("최대공약수:", res)