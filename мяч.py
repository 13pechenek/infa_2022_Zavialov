
import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball():
    '''рисует новый шарик '''
    global x,y,r
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    X.append(x)
    Y.append(y)
    R.append(r)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
def click(event):
    o =False
    for i in range(len(X)):
        if (event.pos[0]-X[i])**2+(event.pos[1]-Y[i])**2<R[i]**2:
         o=True
    return o

pygame.display.update()
clock = pygame.time.Clock()
finished = False
score=0
while not finished:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if click(event)==True:
                score+=1
                print(score)
    X=[]
    Y=[]
    R=[] 
    new_ball()
    new_ball()
    new_ball()
    new_ball()
    new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()