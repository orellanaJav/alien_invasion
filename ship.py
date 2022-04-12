import pygame


class Ship:
    """
    Manage the ship
    """

    def __init__(self, ai_game):
        """
        Init the ship and set its initial position

        Parameters
        ----------
            ai_game: AlienInvasion
                - Actual reference to AlienInvasion instance
        """

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Init place each ship in the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """
        Draw the ship in its actual position
        """

        self.screen.blit(self.image, self.rect)
