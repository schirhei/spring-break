""" This class is about the monster in castle"""
import pygame
import const

class Monster:
    """
    Creates a monster. It moves naturally up and down
    """
    def __init__(self, screen, name, image, health, ini_x, ini_y):
        self._screen = screen
        self._name = str(name)
        self.x_pos = ini_x
        self.y_pos = ini_y
        self.health = health
        self.image = pygame.image.load(image)
        #animation
        pygame.sprite.Sprite.__init__(self)
        self.appear = False
        self.defend = False
        self.half_dead = False


    def return_name(self):
        return self._name

    def return_image(self):
        return self.image

    def return_health(self):
        return self.health

    def draw(self):
        self._screen.blit(pygame.transform.scale(self.image, (180, 180)), (self.x_pos, self.y_pos))
        return
    
    def lose_large_health(self):
        self.health -= 20
        return self.health

    def lose_small_health(self):
        self.health -= 2
        return self.health

    def move(self):
        """
        Contains automatically move, if the wizard won, it will jumps up,
        and the image

        :return:
        """
        if self.x_pos < const.screenwidth:
            self.x_pos += 1
        self.x_pos = self.x_pos

        self.draw()
        return

    def monster_dead(self):
        """
        :return: the monster will be down on the ground
        """
        if self.health == 0:
            self.y_pos = 50
            """Change another image when you are death and print the new quote, same way 
            like how it is dead"""
            m_img = pygame.image.load('')

    def draw_health_bar(self, health):
        """change the rectangle size """
        x = 30
        y = health
        if health > 0:
            pygame.draw.rect(self._screen, (255, 0, 0), (460, 180, x, y), 0)
