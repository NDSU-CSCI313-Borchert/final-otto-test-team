import pygame
import game.constants as constants

from game.level_manager import *
from game.screen import *

class GameScreen(Screen):
    def __init__(self):
        #Not good practice! Should be a separate object
        self._size = 50
        self._rect_x = 50
        self._rect_y = 50
        self._rect_change_x = 2
        self._rect_change_y = 2

    def handle_keyboard_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                LevelManager().leave_level()

    def update(self):
        #Move the object based on the speed
        self._rect_x += self._rect_change_x
        self._rect_y += self._rect_change_y
     
        # Bounce the square if needed
        if self._rect_y > constants.SCREEN_HEIGHT - self._size or self._rect_y < 0:
            self._rect_change_y = self._rect_change_y * -1
        if self._rect_x > constants.SCREEN_WIDTH - self._size or self._rect_x < 0:
            self._rect_change_x = self._rect_change_x * -1
        
    def draw(self, screen):
        # Clear the screen
        screen.fill(constants.WHITE)
     
        # Draw everything
        pygame.draw.rect(screen, constants.BLACK, [self._rect_x, self._rect_y, self._size, self._size])
        pygame.draw.rect(screen, constants.RED, [self._rect_x + 10, self._rect_y + 10, self._size * 3 / 5, self._size * 3 / 5])
 
