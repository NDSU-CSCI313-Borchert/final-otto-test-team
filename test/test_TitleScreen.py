from unittest.mock import patch
from unittest.mock import Mock

import unittest

from title_screen import TitleScreen
from level_manager import LevelManager

class test_TitleScreen(unittest.TestCase):
    @patch('title_screen.pygame') # Needed to build the TitleScreen object
    def test_TitleScreen_draws_something(self, mock_pygame):
        ts = TitleScreen()
        
        # We don't want to create a whole screen, so just Mock the object
        mock_screen = Mock()

        # Call the function under test
        ts.draw(mock_screen)

        # And check to make sure it called screen.blit (i.e. It either displayed text or an image)
        self.assertTrue(mock_screen.blit.called, "Did not display text or an image on the screen!")


    @patch('title_screen.pygame') # Needed to build the TitleScreen object
    def test_TitleScreen_unloads_level_on_esc_keypress(self, mock_pygame):
        ts = TitleScreen()

        # Assumes the LevelManager has been fully tested
        #  (could hypothetically mock this too, if it hasn't been developed yet)
        LevelManager().load_level(ts)

        # Fake that we've pressed the ESCAPE key
        event = Mock()
        event.type = mock_pygame.KEYDOWN
        event.key = mock_pygame.K_ESCAPE
        ts.handle_keyboard_event(event)
        
        # And check if we've removed the level from the screen
        self.assertIsNone(LevelManager().get_current_level())


if __name__ == '__main__':
    unittest.main()
