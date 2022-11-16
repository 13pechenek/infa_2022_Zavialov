import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 0.5
s1=False
screen = pygame.display.set_mode((1200, 900))
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball(x, y, r, color):
    '''рисует новый шарик '''
    circle(screen, color, (x, y), r)


def click(event):
    o = False
    for i in range(len(X)):
        if (event.pos[0]-X[i])**2+(event.pos[1]-Y[i])**2<R[i]**2:
            o = True
            if i == len(X) - 1 and s == True:
                s1 = True
    return o, s1

pygame.display.update()
clock = pygame.time.Clock()
finished = False
score=0
while not finished:
    X=[]
    Y=[]
    R=[]
    VX=[]
    VY=[]
    C=[]
    s=False 
    i=30
    for j in range(i):
        X.append(randint(100, 1000))
        Y.append(randint(200, 700))
        R.append(randint(10,100))
        VX.append(randint(-5, 5))
        VY.append(randint(-5, 5))
        C.append(COLORS[randint(0,5)])
        if randint(1,10)==1:
            s=True
    if s ==True:
        X.append(randint(100, 1000))
        Y.append(randint(200, 700))
        R.append(randint(10,100))
        VX.append(randint(-5, 5))
        VY.append(randint(-5, 5))
        vr=R[i]/600
        vr1=0
    for k in range(600):
        clock.tick(120)
        if s==True:
            new_ball(X[i],Y[i],R[i],COLORS[randint(0,5)]) 
            if X[i]+R[i]+VX[i]>=1200 or X[i]-R[i]+VX[i]<=0:
                VX[i]=-VX[i]
            elif Y[i]+R[i]+VY[i]>=900 or Y[i]-R[i]+VY[i]<=15:
                VY[i]=-VY[i]
            X[i]+=VX[i]
            Y[i]+=VY[i]
            vr1+=vr
            if vr1>=1:
                R[i]-=vr1
                vr1-=1
        for j in range(i):
            new_ball(X[j],Y[j],R[j],C[j])
        for j in range(i):
            if X[j]+R[j]+VX[j]>=1200 or X[j]-R[j]+VX[j]<=0:
                VX[j]=-VX[j]
            elif Y[j]+R[j]+VY[j]>=900 or Y[j]-R[j]+VY[j]<=15:
                VY[j]=-VY[j]
            X[j]+=VX[j]
            Y[j]+=VY[j]
        pygame.display.update()
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if click(event)[0]==True:
                    score+=100
                    if click(event)[1]==True:
                        score+=900
                    print(score)
pygame.quit()