import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Manage bullets fired from the ship"""

    def __init__(self, aa_game):
        super().__init__()

        """Init the bullets and set their starting position"""
        self.screen = aa_game.screen
        self.settings = aa_game.settings
        self.color = aa_game.settings.bullet_color

        # Setting a Rect for bullet and then putting it at correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = aa_game.ship.rect.midtop

        # Store the bullet position as float
        self.bullet_y = float(self.rect.y)


    def update(self):
        """Moving the bullet up in the screen"""
        # Update the float y position of the bullet, bullet's x position never changes once its fired
        self.bullet_y -= self.settings.bullet_speed
        self.rect.y = int(self.bullet_y)


    def draw_bullet(self):
        """Draw the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)