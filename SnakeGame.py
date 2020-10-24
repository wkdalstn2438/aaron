import pygame, random
from datetime import datetime
from datetime import timedelta

# 스크린의 크기 정의
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
BLOCK_SIZE = 25

# 게임에 사용할 색상을 미리 만든다 (RGB)
RED = (255, 0, 0)
GREEN = (0, 255,0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)

# pygame 모듈을 사용하기 전에 초기화
pygame.init()

# 지정한 크기의 창을 생성
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# 사각형을 그리는 함수
def draw_background(screen):
    background = pygame.Rect((0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.draw.rect(screen, WHITE ,background)

def draw_block(screen, color, position):
    block = pygame.Rect(
        (position[0]*BLOCK_SIZE, position[1]*BLOCK_SIZE),
        (BLOCK_SIZE, BLOCK_SIZE)
    )
    pygame.draw.rect(screen, color, block)

def draw_lines(screen, color):
    for i in range(int(SCREEN_WIDTH/20)):
        pygame.draw.line(screen, color, (i*BLOCK_SIZE, 0), (i*BLOCK_SIZE, SCREEN_HEIGHT), 1)
        pygame.draw.line(screen, color, (0, i*BLOCK_SIZE), (SCREEN_WIDTH, i*BLOCK_SIZE), 1)

# 뱀이 움직이는 방향에 대한 오프셋
class Offset:
    NONE = [0, 0]
    RIGHT = [1, 0]
    LEFT = [-1, 0]
    UP = [0, -1]
    DOWN = [0, 1]

# 뱀의 위치와 방향, 색을 정의하는 클래스
# TODO: 방향 바꾸기
# TODO: 자라나기
class Snake:
    # 생성시 뱀의 색상과 위치, 초기에 움직일 방향을 입력
    def __init__(self, color, position, offset):
        self.color = color
        self.offset = offset
        self.positions = [
            position,                           # 머리
            [position[0], position[1] + 1],     # 꼬리 1
            [position[0], position[1] + 2],     # 꼬리 2
            [position[0], position[1] + 3]      # 꼬리 3
        ]

    def draw(self):
        for position in self.positions:
            draw_block(screen, self.color, position)

    def move(self):
        now_position = [self.positions[0][0], self.positions[0][1]]
        self.positions[0][0] += self.offset[0]
        self.positions[0][1] += self.offset[1]
        last_position = now_position
        for i in range(1, len(self.positions)):
            now_position = [self.positions[i][0], self.positions[i][1]]
            self.positions[i] = last_position
            last_position = now_position
    def growth(self):
        end_tail = self.positions[-1]
        front_tail = self.positions[-2]
        # 늘려줄 꼬리의 위치에 대한 좌표계산
        xdiff = end_tail[-1]
        ydiff = end_tail[-2]
        self.positions.append([end_tail[0] + xdiff, end_tail[1] + ydiff])


    pass

# 사과의 색과 위치를 정의하는 클래스
class Apple:
    # 생성시 사과의 위치와 색상을 입력한다.
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def draw(self):
        draw_block(screen, self.color, self.position)
    pass

# 뱀 게임을 정의하는 클래스
# TODO: 자기 위에 뱀과 사과 놓기 (__init__함수에 의한 정의 동작)
# # TODO: 사과 없어지면 새로 놓기
# TODO: 게임을 한 차례 진행하기
class Game:
    def __init__(self, snake, apple):
        self.snake = snake
        self.apple = apple
    def draw(self):
        draw_background(screen)
        self.apple.draw()
        self.snake.draw()
        pygame.display.update()

    def iscrashed(self):
        snake_head = self.snake.positions[0]
        #꼬리가 머리에 닿은경우 ㅣㄹ턴 트루
        if snake_head in self.snake.positions[1:]:
            return True
        if snake_head[0] > 19 or snake_head[1] > 19 or snake_head[0] < 0 or snake_head[1] < 0:
            return True
        return False

    def start(self):
        last_movement = datetime.now()
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and self.snake.offset != Offset.LEFT:
                        self.snake.offset = Offset.RIGHT
                    elif event.key == pygame.K_LEFT and self.snake.offset != Offset.RIGHT:
                        self.snake.offset = Offset.LEFT
                    elif event.key == pygame.K_DOWN and self.snake.offset != Offset.UP:
                        self.snake.offset = Offset.DOWN
                    elif event.key == pygame.K_UP and self.snake.offset != Offset.DOWN:
                        self.snake.offset = Offset.UP
            if timedelta(milliseconds=300) <= datetime.now() - last_movement:
                self.snake.move()
                last_movement = datetime.now()
            if self.apple.position == self.snake.positions[0]:
                self.apple.position = [random.randint(0,19), random.randint(0,19)]
                self.snake.growth()
            if self.iscrashed():
                break

            self.draw()
    pass

game = Game(
    Snake(GREEN, [9, 9], Offset.RIGHT),
    Apple(RED, [5, 5])
)
game.start()