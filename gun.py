import math
from random import choice

import pygame


FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = float(0)
        self.vy = float(0)
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки.
        То есть, обновляет значения self.x и self.y с учетом скоростей
        self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.x += self.vx
        self.y -= self.vy
        self.vy -= 2
        if self.x + 10 >= WIDTH or self.x - 10 <= 0:
            self.vx = -self.vx
        if self.y - self.vy + 10 >= HEIGHT or self.y - self.vy - 10 <= 0:
            if self.vy <= 0 and self.vy >= -3:
                self.vy = 0
            self.vy = -self.vy//5
            self.vx *= 0.8

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью,
         описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели.
            В противном случае возвращает False.
        """
        if (self.r + obj.r)**2 >= (self.x - obj.x)**2 + (self.y - obj.y)**2:
            return True
        else:
            return False


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча
        vx и vy зависят от положения мыши.
        """
        global BALLS, BULLET
        BULLET += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2(
            (event.pos[1]-new_ball.y),
            (event.pos[0]-new_ball.x)
            )
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = -self.f2_power * math.sin(self.an)
        BALLS.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        """
            aaa
        """
        pygame.draw.line(
            self.screen,
            self.color,
            (20, 450),
            (
                math.cos(self.an)*self.f2_power + 20,
                math.sin(self.an)*self.f2_power + 450),
            20
            )

    def power_up(self):
        """
            a
        """
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self):
        self.points = 0

    def new_target(self):
        """ Инициализация новой цели. """
        self.x = choice([600, 780])
        self.y = choice([300, 550])
        self.r = choice([10, 50])
        self.vx = choice([0, 3])
        self.vy = choice([0, 3])
        self.color = RED

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        pygame.draw.circle(
            screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def move(self):
        self.x += self.vx
        self.y += self.vy
        if self.x + self.r > WIDTH or self.x - self.r < 0:
            self.vx = -self.vx
        if self.y + self.r > HEIGHT or self.y - self.r < 0:
            self.vy = -self.vy


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
BULLET = 0
BALLS = []
TARGETS = []
live = 0

clock = pygame.time.Clock()
gun = Gun(screen)
finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    if live < 2:
        tar = Target()
        tar.new_target()
        TARGETS.append(tar)
        tar = 0
        live += 1
    for t in TARGETS:
        t.move()
        t.draw()
    for b in BALLS:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for b in BALLS:
        for t in TARGETS:
            if b.hittest(t):
                live -= 1
                t.hit()
                TARGETS.remove(t)
                BALLS.remove(b)
        b.move()
        if b.y >= 600 - b.r and abs(b.vx) <= 0.001 and abs(b.vy) <= 0.001:
            BALLS.remove(b)
    gun.power_up()

pygame.quit()
