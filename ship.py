import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """This class manages our fighter ship"""

    def __init__(self, aa_game):
        """Init the ship and set its starting position"""
        super().__init__()

        self.moving_right = False
        self.moving_left = False

        self.screen = aa_game.screen
        self.game_settings = aa_game.settings
        self.screen_rect = aa_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Starting ship at bottom center of screen
        self.center_ship()


    def center_ship(self):
        """Center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.ship_x = float(self.rect.x)


    def built_me(self):
        """Draw the ship"""
        self.screen.blit(self.image, self.rect)


    def update(self ):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.ship_x += self.game_settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.ship_x -= self.game_settings.ship_speed

        self.rect.x = int(self.ship_x)

