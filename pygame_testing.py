import pygame
import sys
from const import *

background = pygame.image.load('./assets/cropped/day.png')
tools = ['./assets/original/rope.gif', './assets/original/fish.gif', './assets/original/sunglasses.png', './assets/original/water.gif']
tool1 = pygame.image.load(tools[0])
tool2 = pygame.image.load(tools[1])
tool3 = pygame.image.load(tools[2])

guys = pygame.image.load('./assets/original/guy.gif')
monster = pygame.image.load('./assets/original/wizard.gif')
def main():
    pygame.init()
    screen = pygame.display.set_mode((screenwidth, screenheight))
    screen.fill(white)
    pygame.display.set_caption('Spring Break')

    tool_text = pygame.font.Font.render(pygame.font.Font('C:\\WINDOWS\\Fonts\\times.ttf', 20),'TOOLS:', True, black)
    while True:
        # display bg and "tool"bar
        screen.blit(background, (0,0))
        pygame.draw.rect(screen, white, (0, 0, 340, 80), 0)
        screen.blit(tool_text, (10,30))
        # display tools
        screen.blit(pygame.transform.scale(tool1, (80, 80)), (80,0))
        screen.blit(pygame.transform.scale(tool2, (80, 80)), (160,0))
        screen.blit(pygame.transform.scale(tool3, (80, 80)), (240,0))
        # display characters
        screen.blit(pygame.transform.scale(guys, (100, 180)), (40,170))
        screen.blit(pygame.transform.scale(guys, (100, 180)), (140,170))
        screen.blit(pygame.transform.scale(monster, (180, 180)), (450,170))

        # mouse event
        press = pygame.mouse.get_pressed()[0]
        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]
        if 40 < mouse_x and 170 < mouse_y:
            print(True)
        print( )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()

main()