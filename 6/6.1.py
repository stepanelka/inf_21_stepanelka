import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 2
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball(): #draws a new ball
    global x, y, r
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
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
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            A = pygame.mouse.get_pos()
            x1 = A[0]
            y1 = A[1]
            if ((x1-x)**2 + (y1-y)**2)**0.5 <= r:
                print_screen("yay!")
                n+=1
            else:
                print_screen("click!")
    new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
print('your count', n)
