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

pygame.display.update()
clock = pygame.time.Clock()
finished = False
n = 0
A = []
stars = [new_star() for _ in range(5)]
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            A = pygame.mouse.get_pos()
            x1= A[0]
            y1 = A[1]
            for k in range(1, 5):
                if (((stars[k]['x0']-x1)**2+(stars[k]['y0']-y1)**2)**(1/2))<=stars[k]['r0'] :
                    stars[k] = new_star()
                    print_screen("yay!")
                    n+=3
                if stars[k]['x0'] >= 1200 or stars[k]['y0'] >= 900:
                    stars[k] = new_star()
                    
    pygame.display.update()
    screen.fill(BLACK)
    for k in range(1, 5):
        move(stars[k])
    font = pygame.font.Font(None, 25)
    text = font.render(("Score:" + str(n)), True, [255, 255, 255])
    screen.blit(text, (10, 20))

pygame.quit()
print('your score', n)

