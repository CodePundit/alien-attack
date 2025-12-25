import pygame.font


class Button:
    """A class to show/manage play button"""

    def __init__(self, aa_game, msg):
        """Initializing button attributes"""

        self.game_screen = aa_game.screen

        # Set the size and other properties of the button
        self.width, self.height = 120, 40
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect and center it on the game screen
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.game_screen.get_rect().center

        # Get the button label ready
        """Turn button label into rendered image and center text on the button rect"""
        self.button_label_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.button_label_image_rect = self.button_label_image.get_rect()
        self.button_label_image_rect.center = self.rect.center


    def draw_button(self):
        # First drawing a blank button and then adding label to it
        self.game_screen.fill(self.button_color, self.rect)
        self.game_screen.blit(self.button_label_image, self.button_label_image_rect)

