import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((700, 625))
#colors
skyorange = (254, 213, 162)
skypink = (254, 213, 196)
yellow = (252, 238, 33)
mountain_orange = (252, 152, 49)
mountain_brown = (172, 67, 52)
mountain_purple = (48, 16, 38)
ground_purple = (179, 134, 148)
black = (0, 0, 0)
bird_brown = (66, 33, 11)

rect(screen, skyorange, (0, 0, 700, 140))  # 1я полоса
rect(screen, skypink, (0, 140, 700, 140))  # 2я полоса


def brline(color, x1, y1, x2, y2, x3, y3, l):  # делает заливку для трех точек и линии, ограничивающей их снизу. Или две прямоугольные трапеции, залитые цветом
    polygon(screen, color, [(x1, y1), (x2, y2), (x1, l)]),
    polygon(screen, color, [(x3, y3), (x2, y2), (x3, l)]),
    polygon(screen, color, [(x1, l), (x2, y2), (x3, l)])

#orange mountains
brline(mountain_orange, 5, 280, 8, 250, 160, 130, 280)
brline(mountain_orange, 160, 130, 175, 135, 190, 155, 280)
brline(mountain_orange, 190, 155, 300, 240, 350, 230, 280)
brline(mountain_orange, 350, 230, 375, 243, 425, 210, 280)
brline(mountain_orange, 425, 210, 455, 220, 465, 210, 280)
brline(mountain_orange, 465, 210, 565, 120, 585, 120, 280)
brline(mountain_orange, 585, 120, 615, 150, 635, 145, 280)
brline(mountain_orange, 635, 145, 665, 170, 680, 155, 280)
brline(mountain_orange, 665, 170, 680, 155, 700, 175, 280)

polygon(screen, skypink, [(210, 280), (700, 175), (700, 280)])  # скос
circle(screen, mountain_orange, (572, 121), 12.99)  # вершина правой горы
circle(screen, skypink, (10, 100), 150)  # склон левой горы
circle(screen, skypink, (490, 130), 70)  # склон правой горы
rect(screen, skyorange, (0, 0, 160, 140))  # убирает часть круга, закруглящего склон левой горы
rect(screen, skyorange, (420, 0, 140, 140))  # аналогично для круга от правой горы
polygon(screen, mountain_orange, [(159, 130), (160, 140), (154, 140)])  # треугольник для продолжения горы на новый слой
circle(screen, yellow, (375, 140), 50)  #sun

rect(screen, skyorange, (0, 280, 700, 140))

#brown mountains
polygon(screen, mountain_orange, [(210, 280), (3, 320), (5, 280)])
polygon(screen, mountain_brown, [(50, 420), (0, 320), (0, 420)])
ellipse(screen, mountain_brown, (12, 270, 124, 270))
polygon(screen, mountain_brown, [(50, 420), (0, 320), (0, 420)])
rect(screen, mountain_brown, (0, 400, 700, 20))
polygon(screen, mountain_brown, [(136, 400), (156, 330), (196, 350)])
polygon(screen, mountain_brown, [(196, 350), (216, 290), (256, 300)])
polygon(screen, mountain_brown, [(256, 300), (296, 340), (136, 400)])
polygon(screen, mountain_brown, [(296, 340), (356, 320), (296, 420)])
circle(screen, mountain_brown, (450, 300), 40)
polygon(screen, mountain_brown, [(356, 320), (414, 281), (390, 420)])
polygon(screen, mountain_brown, [(50, 420), (296, 340), (296, 420)])
polygon(screen, mountain_brown, [(296, 420), (356, 320), (390, 420)])
polygon(screen, mountain_brown, [(484, 280), (490, 420), (550, 330)])  # 6
polygon(screen, mountain_brown, [(550, 420), (490, 420), (550, 330)])
polygon(screen, mountain_brown, [(550, 330), (590, 290), (550, 420)])  # 5
polygon(screen, mountain_brown, [(590, 290), (590, 420), (550, 420)])
polygon(screen, mountain_brown, [(590, 290), (590, 420), (620, 300)])  # 4
polygon(screen, mountain_brown, [(620, 420), (590, 420), (620, 300)])
polygon(screen, mountain_brown, [(620, 300), (620, 420), (650, 285)])  # 3
polygon(screen, mountain_brown, [(650, 420), (620, 420), (650, 285)])
polygon(screen, mountain_brown, [(650, 285), (650, 420), (670, 290)])  # 2
polygon(screen, mountain_brown, [(670, 420), (650, 420), (670, 290)])
polygon(screen, mountain_brown, [(670, 290), (700, 210), (670, 420)])  # 1
polygon(screen, mountain_brown, [(700, 420), (700, 210), (670, 420)])
rect(screen, mountain_brown, (386, 305, 120, 100))

rect(screen, ground_purple, (0, 420, 700, 280))  # 4я полоса


brline(mountain_purple, 0, 320, 100, 350, 250, 575, 625)
brline(mountain_purple, 250, 575, 375, 600, 490, 540, 625)
brline(mountain_purple, 490, 540, 555, 560, 650, 420, 625)

circle(screen, ground_purple, (322, 545), 76)  # закругляет слева
polygon(screen, mountain_purple , [(555, 560), (535, 555), (580, 515)])  # убирает неровности в горе
circle(screen, ground_purple, (540, 515), 40)  # закругляет гору справа
circle(screen, mountain_purple , (676, 425), 25)  # вершина горы справа
rect(screen, mountain_purple, (651, 425, 50, 200))  # заливает оставшуюся часть горы
polygon(screen, mountain_purple, [(676, 400), (700, 398), (700, 425)])  # убирает все оставшиеся пробелы


def el_an(surface, color, rect, angle, width=0): #повернутый эллипс
    target_rect = pygame.Rect(rect)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.ellipse(shape_surf, color, (0, 0, *target_rect.size), width)
    rotated_surf = pygame.transform.rotate(shape_surf, angle)
    surface.blit(rotated_surf, rotated_surf.get_rect(center = target_rect.center))

def bird(x, y, l, h): 
    el_an(screen, bird_brown, (x - l, y - h, l, h), -30)
    el_an(screen, bird_brown, (x, y - h, l, h), 30)
    polygon(screen, bird_brown, [(x - 2 * l / 3, y - h / 2), (x, y + 1.5 * h), (x + 2 * l / 3, y - h/ 2), (x, y + h / 2)])

# bird center
bird(300, 220, 25, 5) 
bird(370, 228, 30, 6) 
bird(370, 265, 35, 7)
bird(270, 295, 25, 5) 
bird(450, 430, 30, 6)
bird(480, 470, 30, 6)
bird(540, 510, 35, 7)
bird(570, 460, 30, 6)



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
