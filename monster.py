""" This class is about the monster in castle,
wizard appear, ways to solve it is you need a fish and a sun glasses"""
import pygame
import const

"""
    import image wizard
"""

class Monster(pygame.sprite.Sprite):
    """
    Creates a devil Wizard. It moves naturally up and down
    """

    def __init__(self,monster,screen, name, health, ini_x, ini_y):
        self._screen = screen
        self._name = str(name)
        self.x_pos = ini_x
        self.y_pos = ini_y
        self.health = int(health)
        self.m_img = pygame.image.load('/Users/lenguyen/spring-break/assets/original/wizard.gif')
        #animation part
        self.monster = monster
        pygame.sprite.Sprite.__init__(self)
        self.appear = False
        self.defend = False
        self.half_dead = False

    def name(self, name):
        return name

    def m_img(self):
        if self._name != 'snake':
            self.m_img = pygame.image.load('/Users/lenguyen/spring-break/assets/original/snake.gif')
        if self._name != 'ghost':
            self.m_img = pygame.image.load('/Users/lenguyen/spring-break/assets/original/ghost.gif')
        if self._name != 'monster':
            """edit the photos of the monster"""
            self.m_img = pygame.image.load('/Users/lenguyen/spring-break/assets/original/....')

    def draw(self):
        self._screen.blit(self.m_img, (self.x_pos, self.y_pos))
        return

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

    def load_imgaes(self):
        """put them in temporary position - when the monster die"""
        self.appear = [self._screen.blit(self.m_img_appear, (self.x_pos, self.y_pos)),
                       self._screen.blit(self.m_img, (self.x_pos + 20, self.y_pos + 30))]

        self.defend = [self._screen.blit(self.m_img_defend, (self.x_pos + 20, self.y_pos + 30)),
                       self._screen.blit(self.m_img_appear, (self.x_pos, self.y_pos))]

        self.half_dead = [self._screen.blit.self.m_img_appear, (self.x_pos, self.y_pos),
                          self._screen.blit(self.m_img(self.x_pos + 20, self.y_pos))]
        self.dead = []
        for frame in self.dead:
            self.dead.append(pygame.transform.flip(frame, True, False))

    def draw_health_bar(self):
        """change the rectangle size """
        x = 40
        y = 30
        pygame.draw.rect(self._screen, (255, 0, 0), pygame.Rect(0, 0, x, y))
        while self.defend == True:
            x = x - 10
            y = y - 10
            pygame.draw.rect(self._screen,(255, 0,0), pygame.Rect(0,0,x,y))
            if (x == 0) and ( y==0):
                break
        self.monster_dead()

