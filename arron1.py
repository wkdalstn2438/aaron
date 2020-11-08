"""
a=3
b=3.1
c="123"
print(a)
print(b)
print(c)
print(type(a))

a = int(input())

a = int(input("숫자를 입력하세요:"))
if(a%2==0):
    print("even")
else:
    print("add")

for a in range(10,0,-1):
    print(a)

for a in range(1,5):
    print(a*"*")

for a in range(2,13):
    for b in range(1, 13):
        print(a*b)
    print()
"""
"""
import random

class makeCharacter:

    def __init__(self,id):
        self.name = id
        self.hp = random.randrange(450, 890)
        self.mp = random.randrange(400, 670)
        self.q = random.randrange(70, 80)
        print("{}가 생성되었습니다.\nhp:{}\nmp:{}\n공격력:{}".format(self.name, self.hp, self.mp, self.q))

    def attack(self):
        return self.q

    def attacked(self, atk):
        self.hp = self.hp - atk

    def skill(self):
        self.mp -= 150
        return self.q*2

    def run(self):
        self.hp -= self.hp



id = input("Enter character id:")
ogar = makeCharacter(id)

id = input("Enter character id:")
mc = makeCharacter(id)

while True:
    select_skill = int(input("1.attack 2.skill 3.run"))
    if select_skill == 3:
        mc.run()
        print("{}가 도망갔다.".format(mc.name))
        break
    if select_skill == 1:
        a = mc.attack()
        ogar.attacked(a)
        if ogar.hp <= 0:
            print("{} 사망".format(ogar.name))
            break
        else:
            print("{}가 {}를 {}의 공격력으로 공격했다.\n{}의 hp:{}\n{}의 hp:{}"
            .format(mc.name, ogar.name, a, mc.name, mc.hp, ogar.name, ogar.hp))
    elif select_skill == 2:
        if mc.mp > 0:
            a = mc.skill()
            ogar.attacked(a)
        if ogar.hp <= 0:
            print("{} 사망".format(ogar.name))
            break
        else:
            print("{}가 {}를 스킬로 공격했다.\n{}의 hp:{} mp:{}\n{}의 hp:{}"
            .format(mc.name, ogar.name, mc.name, mc.hp, mc.mp, ogar.name, ogar.hp))
    else:
        print("마나부족")
        continue
    ogar_rand = select_skill = int(input("1.attack 2.skill 3.run"))
    if select_skill == 3:
        ogar.run()
        print("{}가 도망갔다.".format(ogar.name))
        break
    if ogar_rand == 1:
        a = ogar.attack()
        mc.attacked(a)
        if mc.hp <= 0:
            print("{} 사망".format(mc.name))
            break
        else:
            print("{}가 {}를 {}의 공격력으로 공격했다.\n{}의 hp:{}\n{}의 hp:{}"
            .format(ogar.name, mc.name, a, mc.name, mc.hp, ogar.name, ogar.hp))
    elif ogar_rand == 2:
        if ogar.mp > 0:
            a = ogar.skill()
            mc.attacked(a)
        if mc.hp <= 0:
            print("{} 사망".format(mc.name))
            break
        else:
            print("{}가 {}를 스킬로 공격했다.\n{}의 hp:{} mp:{}\n{}의 hp:{}"
            .format(ogar.name, mc.name, ogar.name, ogar.hp, ogar.mp, mc.name, mc.hp))
    else:
        print("마나부족")
        continue
"""
"""
import random

class makemonster:

    def __init__(self,id):
        self.name = id
        self.hp = random.randrange(1200, 1450)
        self.q = random.randrange(30, 39)
        self.l = random.randrange(1, 3)
        print("야생의 {}가 나타났다.\nhp:{}\n공격력:{}".format(self.name, self.hp, self.q))

    def attack(self):
        return self.q

    def attacked(self, atk):
        self.hp = self.hp - atk


class makemc:
    def __init__(self,id):
        self.name = id
        self.lv = 1
        self.hp = random.randrange(480, 780)
        self.q = random.randrange(100, 190)
        self.mp = random.randrange(480, 540)
        self.s = random.randrange(300, 500)
        print("{}가 생성되었습니다.\nlv:{}\nhp:{}\nmp:{}\n공격력:{}\n주문력:{}".format(self.name, self.lv, self.hp, self.mp, self.q, self.s))

    def attack(self):
        return self.q

    def attacked(self, atk):
        self.hp = self.hp - atk

    def skill(self):
        self.mp -= 80
        return self.s

    def level(self):
        self.hp = self.hp + random.randrange(400, 600)
        self.q = self.q + random.randrange(10, 30)
        self.s = self.s




id = "ogar"
ogar = makemonster(id)

id = input("Enter character id:")
mc = makemc(id)

while True:
    select_skill = int(input("1.attack 2.skill"))
    if select_skill == 1:
        a = mc.attack()
        ogar.attacked(a)
        if ogar.hp <= 0:
            print("{} 사망".format(ogar.name))
            print("{}가 {}레벨업".format(mc.name, ogar.l))
            mc.lv = mc.lv + ogar.l
            ch=int(input("1.stop 2.continue"))
            if ch == 1:
                exit()
            else:
                ogar.hp = random.randrange(1200, 1450)
                ogar.q = random.randrange(30, 100)
                print("야생의 {}가 나타났다.\nhp:{}\n공격력:{}".format(ogar.name, ogar.hp, ogar.q))
                continue
        else:
            print("{}가 {}를 {}의 공격력으로 공격했다.\n{}의 hp:{}\n{}의 hp:{}"
            .format(mc.name, ogar.name, a, mc.name, mc.hp, ogar.name, ogar.hp))
    elif select_skill == 2:
        if mc.mp > 0:
            a = mc.skill()
            ogar.attacked(a)
            if ogar.hp <= 0:
                print("{} 사망".format(ogar.name))
                print("{}가 {}레벨업".format(mc.name, ogar.l))
                mc.lv = mc.lv + ogar.l
                ch = int(input("1.stop 2.continue"))
                if ch == 1:
                    exit()
                else:
                    ogar.hp = random.randrange(1200, 1450)
                    ogar.q = random.randrange(30, 50)
                    print("야생의 {}가 나타났다.\nhp:{}\n공격력:{}".format(ogar.name, ogar.hp, ogar.q))
                    continue
            else:
                print("{}가 {}를 스킬로 공격했다".format(mc.name, ogar.name,))
                print("{}가 {}에세 {}에 데미지를 입혔다.\nmp:{}\n{}의 hp:{}".format(mc.name, ogar.name, mc.s, mc.mp, ogar.name, ogar.hp))
        else:
            print("마나부족")
            continue
    ogar_rand = 1
    if ogar_rand == 1:
        a = ogar.attack()
        mc.attacked(a)
        if mc.hp <= 0:
            print("{} 사망".format(mc.name))
            break
        else:
            print("{}가 {}를 {}의 공격력으로 공격했다.".format(ogar.name, mc.name, ogar.q))
            print("{}가 {}데미지를 입었다.\n{}의 hp:{}".format(mc.name, ogar.q, mc.name, mc.hp))
        continue
"""
"""
list = [3, 5, 1, 2, 7]

for i in range(len(list)):
    for i in range(len(list) - 1):
        if list[i] > list[i+1]:
            list[i], list[i+1] = list[i+1], list[i]

print(list)
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
carImg = pygame.image.load('')

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