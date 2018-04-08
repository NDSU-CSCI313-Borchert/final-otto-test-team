import pygame
import constants

from screen import *
from level_manager import *
from game_screen import *

class TitleScreen(Screen):
    def __init__(self):
        #Because this text never changes, we can load it in the constructor
        #Otherwise, we may need to move render into draw
        font = pygame.font.SysFont('Calibri', 25, True, False)

        #The underscore character indicates that this is a private instance variable
        self._text = font.render("Otto's Game Template",True,constants.BLACK)

    def handle_keyboard_event(self, event):
        if event.type == pygame.KEYDOWN:
            # An argument can be made to place leaving the level in the main loop
            if event.key == pygame.K_ESCAPE:
                LevelManager().leave_level()
            elif event.key == pygame.K_p:
                LevelManager().load_level(GameScreen())

    #No need to do anything here, unless we've got some animation
    def update(self):
        pass
        
    def draw(self, screen):
        # Clear the screen
        screen.fill(constants.WHITE)
     
        # Draw my title text!
        screen.blit(self._text, [250, 250])
