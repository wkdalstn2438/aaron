"""
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
crashed = False
carImg = pygame.image.load('car (1).jpg')


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

    y += y_change
    gameDisplay.fill(white)
    car(carImg, x, y)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
"""
"""
def enqueue(queue, date):
    if len(queue) >= max:
        print("overflow")
        return
    else:
        queue.append(data)

    return queue

def dequeue(queue):
    if len(queue) == 0:
        print("underflow")
        return
    else:
        print(queue[0])
        del queue[0]

    return queue

max = 5
queue = []
while True:
     a = int(input("1 is equeue, 2 is dequeue, 3 is out :"))

     if a == 1:
         data = int(input("Enter the data :"))
         queue = enqueue(queue, data)

     elif a == 2:
         queue = dequeue(queue)

     elif a == 3:
         print("out")
         break
"""
a = [5, 1, 4, 2]

for i in range(len(a)):
        print(a[i])