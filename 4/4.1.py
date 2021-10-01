import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))

#colors
yellow = (255, 240, 0)
red = (255, 31, 0)
black = (0, 0, 0)

#drawing 
circle(screen, yellow, (300, 300), 200) #yellow circle 
circle(screen, red, (240, 250), 40) #red eye left
circle(screen, red, (360, 250), 35) #red eye right 
circle(screen, black, (300, 300), 200, 2) #cont of yellow circle
circle(screen, black, (240, 250), 40, 2) #cont of left eye 
circle(screen, black, (360, 250), 35, 2) #cont of right eye 
circle(screen, black, (240, 250), 20) #pupil left
circle(screen, black, (360, 250), 20) #pupil right 
rect(screen, black, (225, 400, 150, 30)) #background 
polygon(screen, black, [(250, 200), (200, 150), (260, 220), (210, 140)]) #eyebrow left
polygon(screen, black, [(350, 200), (400, 150), (340, 220), (390, 140)]) #eyebrow right 


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
