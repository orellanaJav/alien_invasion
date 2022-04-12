import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """
    General class to manage the resources and the behavior of the game
    """

    def __init__(self):
        """
        Init the game a create the resources
        """

        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')

        self.ship = Ship(self)

    def run_game(self):
        """
        Init the main bucle for the game
        """

        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """
        Search for events in keyboard and mouse
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move ship to the right
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    # Move ship to the left
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        """
        Redraw screen in every step by bucle
        """

        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Make visible the last screen drawed
        pygame.display.flip()


if __name__ == '__main__':
    """
    Make an instance of the game and run it
    """

    ai = AlienInvasion()
    ai.run_game()
