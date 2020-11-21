"""
value = int(input("Enter the value"))

if value % 2 == 1:
    print("even")

else:
    print("add")

for i in range(5):
    print("*" * i)
for i in range(5):
    print("*" * (5 - i))

a = 1

while a <= 10:
    print("*" * a)
    a = a + 1

import random

def make_list():
    a = []
    for i in range(100):
        a.append(random.randrange(1, 100))

    return a

def insert_sort(a):
    for i in range(1, len(a)):

        for j in range(i, 0, -1):
            if a[j-1] > a[j]:
                a[j], a[j-1] = a[j-1], a[j]

    return a

not_sort_list = make_list()
sort_list = insert_sort(not_sort_list)
print(sort_list)
"""
import pygame
pygame.init()

def car(carImg, x, y):
    gameDisplay.blit(carImg, (x, y))

display_width = 800
display_height = 600
car_width = 0
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('race')
black = (0, 0, 0)
white = (255, 255, 255)
clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load('car.jpg')

def car(carImg, x, y):
    gameDisplay.blit(carImg, (x, y))

def text_objects(text, font):
    textSurface = font.render(text, )
x = (display_width * 0.45)
y = (display_height * 0.8)
x_change = 0
y_change = 0
car_spead = 0
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
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                y_change = 0
    x += x_change

    gameDisplay.fill(white)
    car(carImg, x, y)

    if x > display_width - car_width or x < 0:
        crash()
    y += y_change
    gameDisplay.fill(white)
    car(carImg, x, y)
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()