import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

color = (255, 255, 0)
polygon(screen,(255,255,255),[(0,0),(400,0),(400,400),(0,400)])
circle(screen,color,(150,150),100)
circle(screen,(0,0,0),(150,150),100,2)
line(screen,(0,0,0),(100,200),(200,200),20)

circle(screen,(255,0,0),(100,130),25)
circle(screen,(0,0,0),(100,130),25,1)
circle(screen,(255,0,0),(200,130),20)
circle(screen,(0,0,0),(200,130),20,1)
circle(screen,(0,0,0),(100,130),10)
circle(screen,(0,0,0),(200,130),10)
polygon(screen,(0,0,0),[(50,55),(60,45),(135,108),(125,118)])
polygon(screen,(0,0,0),[(164,110),(170,120),(250,82),(244,72)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()