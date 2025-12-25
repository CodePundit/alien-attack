import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """This class to represent a single Alien in the fleet"""

    def __init__(self, aa_game):
        """Init the Alien and set its starting position"""

        super().__init__()

        self.game_screen = aa_game.screen
        self.game_settings = aa_game.settings

        # Load the Alien image and get its rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Store the alien's exact horizontal position
        self.x_position = float(self.rect.x)


    def update(self):
        """Move the alien right or left"""
        self.x_position += (self.game_settings.alien_horizontal_speed * self.game_settings.alien_fleet_direction)
        self.rect.x = int(self.x_position)


    def check_edges(self):
        """Return True if an alien is at the edge of screen"""
        if self.rect.left <= 0 or self.rect.right > self.game_screen.get_rect().right:
            return True
        else:
            return False


    def drop_alien_location(self):
        self.rect.y += self.game_settings.alien_fleet_drop_speed

