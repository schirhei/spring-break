"""
    this class is to create motions of weapon, how it attacks the monster

"""
import const
import pygame


class Tool:
    """
    This class return weapon name and weapon direction

    """
    def __init__(self, screen, image, name, ini_x, ini_y):
        self.screen = screen
        self.name = name
        self.image = pygame.image.load(image)
        self.x_pos = int(ini_x)
        self.y_pos = int(ini_y) 
    
    def return_name(self):
        return self.name

    def return_image(self):
        return self.image

    def draw(self):
        self.screen.blit(pygame.transform.scale(self.image, (80, 80)), (self.x_pos, self.y_pos))  
        return

    def move_weapon(self):
        if self.x_pos < const.screenwidth:
            self.x_pos += 1
        else:
            self.x_pos = 0
        self.draw()
