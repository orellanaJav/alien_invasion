import sys

import pygame

from settings import Settings


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

    def run_game(self):
        """
        Init the main bucle for the game
        """

        while True:
            # Search for events in keyboard and mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw screen in every step by bucle
            self.screen.fill(self.settings.bg_color)

            # Make visible the last screen drawed
            pygame.display.flip()


if __name__ == '__main__':
    """
    Make an instance of the game and run it
    """

    ai = AlienInvasion()
    ai.run_game()
