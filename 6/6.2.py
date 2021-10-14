import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 25
width = 1200
height = 900
screen = pygame.display.set_mode((width, height))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

balls = []
stars = []
def new_ball():
    x = randint(100,1100)
    y = randint(100,800)
    Vx = randint(-10, 10)
    Vy = randint(-10, 10)
    color =COLORS[randint(0, 5)]
    r = randint(10, 100) 
    balls.append([x, y, r, color, Vx, Vy])
    
def new_star():
    x = randint(100,1100)
    y = 0
    Vx = randint(5, 10)
    Vy = randint(15, 25)
    color =COLORS[randint(0, 5)]
    r = randint(10, 50) 
    stars.append([x, y, r, color, Vx, Vy])
    
def draw_balls():
    for ball in balls:
        circle(screen, ball[3], (int(ball[0]), int(ball[1])), ball[2])

def draw_stars():
    for star in stars:
        x = star[0]
        y = star[1]
        r = star[2]
        polygon(screen, star[3], [(x, y - r), (x + r/5, y - r/5), (x + 7*r/8, y - r/4), (x + r/4, y + r/6), (x + r/2, y + 7*r/8), (x, y + r/3), (x - r/2, y + 7*r/8), (x - r/4, y + r/ 6), (x - 7*r/8, y - r/4), (x - r/5, y - r/5)])

def move_balls():
    for ball in balls:
        x = ball[0]
        y = ball[1]
        r = ball[2]
        vx = ball[4]
        vy = ball[5]
        if (x + r + vx > width or x - r + vx < 0) :
            ball[4] = -ball[4]

        if (y + r + vy > height or y - r + vy < 0) :
            ball[5] = -ball[5]

        ball[0] += ball[4]
        ball[1] += ball[5]

def move_stars():
    for star in stars:
        x = star[0]
        y = star[1]
        r = star[2]
        vx = star[4]
        vy = star[5]
        star[0] += star[4]
        star[1] += star[5]


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
balls = []

def score():
    font = pygame.font.Font(None, 25)
    text = font.render("score: " + str(n), True, [255, 255, 255])
    screen.blit(text, (10, 10))
    
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if len(balls) < 15:
            new_ball()
        if len(stars) < 10:
            new_star()
        if event.type == pygame.MOUSEBUTTONDOWN:
            i = len(balls) - 1
            A = pygame.mouse.get_pos()
            while i in range(len(balls) - 1):
                x = balls[i][0]
                y = balls[i][1]
                r = balls[i][2]
                x1 = A[0]
                y1 = A[1]
                if ((x1-x)**2 + (y1-y)**2) <= r ** 2:
                    print_screen("yay!")
                    balls.pop(i)
                    n += 1
                else:
                    print_screen("click!")
                    i -= 1
        if event.type == pygame.MOUSEBUTTONDOWN:
            i = len(stars) - 1
            A = pygame.mouse.get_pos()
            while i > 0:
                x = stars[i][0]
                y = stars[i][1]
                r = stars[i][2]
                x1 = A[0]
                y1 = A[1]
                if ((x1-x)**2 + (y1-y)**2) <= r ** 2:
                    print_screen("yay!")
                    stars.pop(i)
                    n += 5
                else:
                    print_screen("click!")
                    i -= 1
                if abs(y) > height or abs(x) > width:
                    stars.pop(i)
    move_balls()
    move_stars()
    screen.fill(BLACK)
    draw_balls()
    draw_stars()
    score()
    pygame.display.update()
print('your score', n)  
pygame.quit()
