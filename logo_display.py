import pygame
from pygame.locals import*

img = pygame.image.load('logo.png')


white = (255, 64, 0)
w = 1700
h = 700
new_width  = 200
new_height = 300
picture = pygame.transform.scale(img, (1280, 720))
screen = pygame.display.set_mode((w, h))
screen.fill((white))
running = 1

while running:
    screen.fill((white))
    screen.blit(img,(0,0))
    pygame.display.flip()