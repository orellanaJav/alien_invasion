import sys

import pygame

from bullet import Bullet
from settings import Settings
from ship import Ship


class AlienInvasion:
    """
    General class to manage the resources and the behavior of the game
    """

    def __init__(self):
        """
        Init the game and create resources
        """

        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
        self.bullets = pygame.sprite.Group()

        self.ship = Ship(self)

    def run_game(self):
        """
        Init the main bucle for the game
        """

        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _fire_bullet(self):
        """
        Creates a new bullet and adding to bullets group
        """
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_keydown_events(self, event):
        """
        Responds to keystrokes
        """

        if event.key == pygame.K_RIGHT:
            # Move ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move ship to the left
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """
        Responds to key releases
        """

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_events(self):
        """
        Search for events in keyboard and mouse
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _update_screen(self):
        """
        Redraw screen in every step by bucle
        """

        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Make visible the last screen drawed
        pygame.display.flip()

    def _update_bullets(self):
        """
        Updates the bullets position and removes the old ones
        """
        self.bullets.update()
        # Delete desapear bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)


if __name__ == '__main__':
    """
    Make an instance of the game and run it
    """

    ai = AlienInvasion()
    ai.run_game()
