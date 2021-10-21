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
#отдельно все работает, вместе как-то не очень
def new_star():
    x = randint(100,1100)
    y = 1
    vx = randint(5, 10)
    vy = randint(15, 25)
    color =COLORS[randint(0, 5)]
    r = randint(10, 50) 
    polygon(screen, color, [(x, y - r), (x + r/5, y - r/5), (x + 7*r/8, y - r/4), (x + r/4, y + r/6), (x + r/2, y + 7*r/8), (x, y + r/3), (x - r/2, y + 7*r/8), (x - r/4, y + r/ 6), (x - 7*r/8, y - r/4), (x - r/5, y - r/5)])
    return { 'x0': x,
             'y0': y,
             'r0': r,
             'vx0': vx,
             'vy0': vy,
             'color': color}

def move(star):
    star['x0'] += star['vx0']
    star['y0'] += star['vy0']
    polygon(screen, star['color'], [(star['x0'], star['y0'] - star['r0']), (star['x0'] + star['r0']/5, star['y0'] - star['r0']/5), (star['x0'] + 7*star['r0']/8, star['y0'] - star['r0']/4), (star['x0'] + star['r0']/4, star['y0'] + star['r0']/6), (star['x0'] + star['r0']/2, star['y0'] + 7*star['r0']/8), (star['x0'], star['y0'] + star['r0']/3), (star['x0'] - star['r0']/2, star['y0'] + 7*star['r0']/8), (star['x0'] - star['r0']/4, star['y0'] + star['r0']/ 6), (star['x0'] - 7*star['r0']/8, star['y0'] - star['r0']/4), (star['x0'] - star['r0']/5, star['y0'] - star['r0']/5)])  

def print_screen(word):
    font = pygame.font.Font(None, 25)
    text = font.render(word, True, [255, 255, 255])
    a, b = event.pos
    screen.blit(text, (a - 25, b - 20))

def new_ball():
    x = randint(100, 1100)
    y = randint(100, 900)
    vx = randint(-10, 10)
    vy = randint(-10, 10)
    color = COLORS[randint(0, 5)]
    r = randint(20, 100)
    circle(screen, color, (x, y), r)
    ball = { 'x1': x,
             'y1': y,
             'r1': r,
             'vx1': vx,
             'vy1': vy,
             'color': color}

def move(ball):
    if ((ball['x1'] + ball['r1']) <= 1200) and (ball['x1'] - ball['r1']) >= 0:
        ball ['x1'] += ball ['vx1']
    else:
        ball['vx1']*=-1
        ball['x1']+=ball['vx1']
    
    if ((ball['y1'] + ball['r1']) <= 900) and (ball['y1'] - ball['r1']) >= 0:
        ball['y1'] += ball ['vy1']
    else:
        ball['vy1']*=-1
        ball['y1']+=ball['vy1']
    
    circle (screen, ball['color'], ( ball['x1'], ball ['y1']), ball['r1'])
    

pygame.display.update()
clock = pygame.time.Clock()
finished = False
n = 0
A = []
stars = [new_star() for _ in range(5)]
balls = [new_ball()  for _ in range(10)]
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            A = pygame.mouse.get_pos()
            xp= A[0]
            yp = A[1]
            for k in range(1, 5):
                if (((stars[k]['x0']-xp)**2+(stars[k]['y0']-yp)**2)**(1/2))<=stars[k]['r0'] :
                    stars[k] = new_star()
                    print_screen("yay!")
                    n+=3
                if stars[k]['x0'] >= 1200 or stars[k]['y0'] >= 900:
                    stars[k] = new_star()
            for i in range(0,10):
                if (((balls[i]['x1']-xp)**2+(balls[i]['y1']-yp)**2)**(1/2))<=balls[i]['r'] :
                    balls[i]=new_ball()
                    print_screen("yay!")
                    n+=1       
    pygame.display.update()
    screen.fill(BLACK)
    for k in range(1, 5):
        move(stars[k])
    for i in range (0,10):
        move(balls[i])
    font = pygame.font.Font(None, 25)
    text = font.render(("Score:" + str(n)), True, [255, 255, 255])
    screen.blit(text, (10, 20))

pygame.quit()
print('your score', n)

