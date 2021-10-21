import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 20
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
    x = randint(100, 1100)
    y = randint(100, 900)
    vx = randint(-10, 10)
    vy = randint(-10, 10)
    color = COLORS[randint(0, 5)]
    r = randint(20, 100)
    circle(screen, color, (x, y), r)
    return { 'x': x,
             'y': y,
             'r': r,
             'vx': vx,
             'vy': vy,
             'color': color}

def move(ball):
    if ((ball['x'] + ball['r']) <= 1200) and (ball['x'] - ball['r']) >= 0:
        ball ['x'] += ball ['vx']
    else:
        ball['vx']*=-1
        ball['x']+=ball['vx']
    
    if ((ball['y'] + ball['r']) <= 900) and (ball['y'] - ball['r']) >= 0:
        ball['y'] += ball ['vy']
    else:
        ball['vy']*=-1
        ball['y']+=ball['vy']
    
    circle (screen, ball['color'], ( ball['x'], ball ['y']), ball['r'])
    
def print_screen(word):
    font = pygame.font.Font(None, 25)
    text = font.render(word, True, [255, 255, 255])
    a, b = event.pos
    screen.blit(text, (a - 25, b - 20))

pygame.display.update()
clock = pygame.time.Clock()
finished = False
n = 0
A = []
balls = [new_ball() for _ in range(10)]

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            A = pygame.mouse.get_pos()
            x1= A[0]
            y1 = A[1]
            for i in range(0,10):
                if (((balls[i]['x']-x1)**2+(balls[i]['y']-y1)**2)**(1/2))<=balls[i]['r'] :
                    balls[i]=new_ball()
                    print_screen("yay!")
                    n+=1
    pygame.display.update()
    screen.fill(BLACK)
    for i in range (0,10):
        move(balls[i])

pygame.quit()
print('your score', n)
