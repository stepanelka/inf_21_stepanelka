import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))


circle(screen, (255, 240, 0), (300, 300), 200)
circle(screen, (255, 31, 0), (240, 250), 40)
circle(screen, (255, 31, 0), (360, 250), 35)
circle(screen, (0, 0, 0), (300, 300), 200, 2)
circle(screen, (0, 0, 0), (240, 250), 40, 2)
circle(screen, (0, 0, 0), (360, 250), 35, 2)
circle(screen, (0, 0, 0), (240, 250), 20)
circle(screen, (0, 0, 0), (360, 250), 20)

rect(screen, (0, 0, 0), (225, 400, 150, 30))

polygon(screen, (0, 0, 0), [(250, 200), (200, 150), (260, 220), (210, 140)])
polygon(screen, (0, 0, 0), [(350, 200), (400, 150), (340, 220), (390, 140)])
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
