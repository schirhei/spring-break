"""
    many tips that users click next to read the notes
    when they see the animal to survive
"""
import pygame
from monster import Monster
from const import *
pygame.mouse.set_visible(True)

"""Edit tips to to kill the monster """
tip1 = pygame.image.load('')


class Tip:
    """
    The tip boards just have the specific position and cursor next or preview
    """
    def __init__(self, screen, preview_button, next_button, ini_x, ini_y):
        self.screen = screen
        self.monster = Monster
        self.preview_button = preview_button
        self.next_button = next_button
        self.ini_x = ini_x
        self.ini_y = ini_y

    def tip_collection(self):
        """return the tip collections """
        if self.monster.name == 'Wizard':
            tip1 = pygame.image.load('')
        else:
            tip2 = pygame.image.load('')
        return

    def draw(self):
        screen = pygame.display.set_mode((200,300))

        #to see the mouse position
        event = pygame.event.poll()
        if event.type == pygame.MOUSEMOTION:
            print("mouse at (%d, %d)" % event.pos)

        screen.fill((0,0,0))
        pygame.display.flip()

