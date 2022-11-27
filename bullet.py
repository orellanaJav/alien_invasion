import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """
    Manage the scattered bullets of a ship
    """

    def __init__(self, ai_game):
        """
        Create an object for the bullet at the current position of the sip
        """
        super.__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a rectangle for the bullet in (0, 0) and then set the correct
        # position.

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_heigth)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Save the position of the bullet as decimal
        self.y = float(self.rect.y)

    def update(self):
        """
        Move the bullet up the screen
        """

        # Update the actual decimal position of the bullet
        self.y -= self.settings.bullet_speed
        # Update the rectangule position
        self.rect.y = self.y

    def draw_bullet(self):
        """
        Draw the bullet in the screen
        """
        pygame.draw.rect(self.screen, self.color, self.rect)
