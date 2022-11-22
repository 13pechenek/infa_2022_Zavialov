from random import randint
from pygame.draw import *
import pygame

pygame.init()

FPS = 0.5
screen = pygame.display.set_mode((1200, 900))
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def draw_ball(x_b, y_b, r_b, color):
    """
        Рисует новый шарик:
            x_b - координата по оси x;
            y_b - координата по оси y;
            r_b - радиус шарика;
            color - цвет шарика.
    """
    circle(screen, color, (x_b, y_b), r_b)


def click(eve):
    """
        Проверяет попадание по шарику
    """
    click_in_target = False
    s_1 = False
    for count_1 in enumerate(X):
        if (eve.pos[0]-X[count_1])**2+(eve.pos[1]-Y[count_1])**2<R[i]**2:
            click_in_target = True
            if count_1 == len(X) - 1 and S is True:
                s_1 = True
    return click_in_target, s_1


def gen_balls():
    """
        Заполняет массивы скоростей и координат произвольными значениями
    """
    global S
    for count_2 in range(i):
        X.append(randint(100, 1000))
        Y.append(randint(200, 700))
        R.append(randint(10,100))
        VX.append(randint(-5, 5))
        VY.append(randint(-5, 5))
        C.append(COLORS[randint(0, 5)])
        if randint(1, 10) == 1:
            S = True
    if S is True:
        X.append(randint(100, 1000))
        Y.append(randint(200, 700))
        R.append(randint(10, 100))
        VX.append(randint(-5, 5))
        VY.append(randint(-5, 5))
        global VR, VR1
        VR = R[i]/600
        VR1 = 0


def move_balls():
    """
        Функция перемещает шары в зависимости от скоростей и соударений со стенами
    """
    global VR,  VR1
    if S is True:
        draw_ball(X[i], Y[i], R[i], COLORS[randint(0, 5)])
        if X[i] + R[i] + VX[i] >= 1200 or X[i] - R[i] + VX[i] <= 0:
            VX[i] =- VX[i]
        elif Y[i] + R[i] + VY[i] >= 900 or Y[i] - R[i] + VY[i] <= 15:
            VY[i] =- VY[i]
        X[i] += VX[i]
        Y[i] += VY[i]
        VR1 += VR
        if VR1 >= 1:
            R[i] -= VR1
            VR1 -= 1
    for count_3 in range(i):
        draw_ball(X[count_3], Y[count_3], R[count_3], C[count_3])
    for count_4 in range(i):
        if X[count_4] + R[count_4] + VX[count_4] >= 1200 or X[count_4] - R[count_4] + VX[count_4] <= 0:
            VX[count_4] =- VX[count_4]
        elif Y[count_4] + R[count_4] + VY[count_4] >= 900 or Y[count_4] - R[count_4] + VY[count_4] <= 15:
            VY[count_4] =- VY[count_4]
        X[count_4] += VX[count_4]
        Y[count_4] += VY[count_4]


pygame.display.update()
clock = pygame.time.Clock()
FINISHED = False
SCORE=0
while not FINISHED:
    X = []
    Y = []
    R = []
    VX = []
    VY = []
    C = []
    S = False
    i = 30
    VR = 0
    VR1 = 0
    gen_balls()
    for c in range(600):
        clock.tick(120)
        move_balls()
        pygame.display.update()
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                FINISHED = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if click(event)[0] is True:
                    SCORE += 100
                    if click(event)[1] is True:
                        SCORE += 900
                    print(SCORE)
pygame.quit()
