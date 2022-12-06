"""
Author: Lucas Henrique Messias Gonçalves
Date: september 29th 2022
Function of this code: Create Initial Element on a Screen. 
"""

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

# define sizes of screen
width = 640  # largura
heigh = 480  # altura
screen = pygame.display.set_mode((width, heigh))

x = width/2
y = heigh/2
# renaming the title of screen
pygame.display.set_caption('RPG')

# structure of display the screen, in a loop conditional
while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

            # key actions
        if event.type == KEYDOWN:
            if event.key == K_a:
                x = x - 20
            if event.key == K_d:
                x = x + 20
            if event.key == K_w:
                y = y - 20
            if event.key == K_s:
                y = y + 20

    pygame.draw.rect(screen, (255, 30, 130), (x, y, 40, 50))

    # if y >= heigh:
    #   y = 0
    # y = y + 1
    pygame.display.update()
