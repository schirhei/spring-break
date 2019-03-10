import pygame

import sys
from objects.monster import Monster
from objects.tool import Tool
from environments.env_castle import Castle
from const import *

user_place = input('Where do you want to camp? ')
place = Castle(user_place)
place.requestAPI()
weather = place.getWeather()
if weather == 'Rain' or weather == 'Cloudy':
    background = pygame.image.load('./assets/cropped/cloudy.png')
else:
    background = pygame.image.load('./assets/cropped/day.png')


# tools = { 'rope': './assets/original/rope.gif',
#           'fish': './assets/original/fish.gif',
#           'sunglasses': './assets/original/sunglasses.png',
#           'water': './assets/original/water.gif'}

tools = [
    { 
        'name': 'rope',
        'image': './assets/original/rope.gif'
    },
    { 
        'name': 'fish',
        'image': './assets/original/fish.gif'
    },
    { 
        'name': 'sunglasses',
        'image': './assets/original/sunglasses.png'
    },
    { 
        'name': 'water',
        'image': './assets/original/water.gif'
    },
]

def main():
    pressed = set([])
    tip = ''
    guy1_equip = None
    guy1 = pygame.image.load('./assets/original/guy.gif')
    redguy = pygame.image.load('./assets/original/redguy.png')
    
    pygame.init()
    
    screen = pygame.display.set_mode((screenwidth, screenheight))
    screen.fill(white)
    pygame.display.set_caption('Spring Break')

    tool_text = pygame.font.Font.render(pygame.font.Font('C:\\WINDOWS\\Fonts\\times.ttf', 20),'TOOLS:', True, black)
    
    monster = Monster(screen, 'Wizard', './assets/original/wizard.gif', 200, x_pos, y_pos)
    tool1 = Tool(screen, tools[0]['image'], tools[0]['name'], 80, 0)
    tool2 = Tool(screen, tools[1]['image'], tools[1]['name'], 160, 0)
    tool3 = Tool(screen, tools[2]['image'], tools[2]['name'], 240, 0)


    while (True):
        print(pressed)
        print(tip)
        tip_text = pygame.font.Font.render(pygame.font.Font('C:\\WINDOWS\\Fonts\\times.ttf', 20), tip, True, black)
        # display bg and "tool"bar
        screen.blit(background, (0,0))
        pygame.draw.rect(screen, white, (0, 0, 340, 80), 0)
        screen.blit(tool_text, (10,30))
        screen.blit(tip_text, (360, 30))
        # display tools
        tool1.draw()
        tool2.draw()
        tool3.draw()
        # display characters
        screen.blit(pygame.transform.scale(guy1, (100, 180)), (40,170))

        monster.draw()

        # display equipped tools

        guy1_equip

        monster.draw_health_bar(monster.return_health())
        # mouse event
        press = pygame.mouse.get_pressed()[0]
        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]

        # character and tool clicking
        if 40 < mouse_x and 170 < mouse_y and 140 > mouse_x and 350 > mouse_y and press == 1:
            pressed.add('guy1')
            guy1 = redguy       
        elif 450 < mouse_x and 170 < mouse_y and 630 > mouse_x and 350 > mouse_y and press == 1:
            pressed.add('monster')
            guy = pygame.image.load('./assets/original/guy.gif')
        elif 80 < mouse_x and 0 < mouse_y and 160 > mouse_x and 80 > mouse_y and press == 1:
            pressed.add('tool1')
            guy = pygame.image.load('./assets/original/guy.gif')
        elif 160 < mouse_x and 0 < mouse_y and 240 > mouse_x and 80 > mouse_y and press == 1:
            pressed.add('tool2')
            guy = pygame.image.load('./assets/original/guy.gif')
        elif 240 < mouse_x and 0 < mouse_y and 320 > mouse_x and 80 > mouse_y and press == 1:
            pressed.add('tool3')
            guy = pygame.image.load('./assets/original/guy.gif')

        # give tools to the guys
        if len(pressed) == 2:
            if 'guy1' in pressed and 'tool1' in pressed:
                guy1_equip = Tool(screen, tools[0]["image"], tools[0]["name"], 40, 250)
            elif 'guy1' in pressed and 'tool2' in pressed:
                guy1_equip = Tool(screen, tools[1]["image"], tools[1]["name"], 40, 250)
            elif 'guy1' in pressed and 'tool3' in pressed:
                guy1_equip = Tool(screen, tools[2]["image"], tools[2]["name"], 40, 250)
            guy1_equip.draw()
            if 'guy1' in pressed and 'monster' in pressed and guy1_equip != None and press == 1:
                monster.defend = True
                print(monster.return_health())
                print(guy1_equip.return_name())
                if monster.return_name() == 'Wizard':
                    if guy1_equip.return_name() == 'fish':
                        print('fish is attack')
                        monster.lose_large_health()
                        tip = 'fish is effective against wizard'
                    if guy1_equip.return_name()  == 'sunglasses':
                        monster.lose_large_health()
                        tip = 'sunglasses is effective against wizard' 
                    if guy1_equip.return_name()  == 'rope':
                        monster.lose_small_health()
                        tip = 'rope is not effective against wizard'
        elif len(pressed) >= 2 and ('tool1' in pressed or 'tool2' in pressed or 'tool3' in pressed):
            pressed = set([])
        elif 'guy1' in pressed and 'monster' in pressed:
            pressed = set([])
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
        

main()