from game.level_manager import *
from game.title_screen import *

import pygame
import game.constants as constants
 
# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode([constants.SCREEN_WIDTH,
                                  constants.SCREEN_HEIGHT])
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
level_manager = LevelManager()
level_manager.load_level(TitleScreen())
 
# -------- Main Program Loop -----------
while True: #Continue until quit

    current_level = level_manager.get_current_level()

    #We've left the TitleScreen - Exit the game
    if current_level == None:
        break

    #Update and Draw are very common delinations in game logic
    #Update is inolved in changing game state
    #Draw simply draws objects on the screen
    current_level.update()
    current_level.draw(screen)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)

    #Handle base keyboard event, plus any inherited from the level    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            break
        current_level.handle_keyboard_event(event)
     

pygame.quit()
