import pygame.font
from pygame.sprite import Group

from ship import Ship


class Scoreboard:
    """A class to report Scoring information"""

    def __init__(self, aa_game):
        """Initializing Scorekeeping attributes"""

        self.aa_game = aa_game

        self.font = pygame.font.SysFont(None, 48)
        self.text_color = (30, 30, 30)

        # Get the initial Scoreboard label ready
        self.update_score()
        self._update_high_score()
        self.update_level_number()
        self.update_remaining_ships()


    def update_score(self):
        """Turn Scoreboard label into rendered image and place it at top right"""
        score_str = "{:,}".format(self.aa_game.game_stats.score)

        self.score_label_image = self.font.render(score_str, True, self.text_color, self.aa_game.settings.bg_color)

        # Display the score at top right
        self.score_label_rect = self.score_label_image.get_rect()
        self.score_label_rect.right = self.aa_game.screen.get_rect().right - 20
        self.score_label_rect.top = 20

        self._check_high_score()


    def _check_high_score(self):
        """Check to see if there's a new high score"""
        if self.aa_game.game_stats.score > self.aa_game.game_stats.high_score:
            self.aa_game.game_stats.high_score = self.aa_game.game_stats.score
            self._update_high_score()


    def _update_high_score(self):
        """Turn the High Score into rendered image and place it at center top"""
        high_score = round(self.aa_game.game_stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)

        self.high_score_label_image = self.font.render(high_score_str, True, self.text_color, self.aa_game.settings.bg_color)

        # Display the score at top center
        self.high_score_label_rect = self.high_score_label_image.get_rect()
        self.high_score_label_rect.centerx = self.aa_game.screen.get_rect().centerx
        self.high_score_label_rect.top = self.score_label_rect.top + 12


    def update_level_number(self):
        """Turn the Level number into rendered image and place it at top right below score"""
        level_str = str(self.aa_game.game_stats.level)

        self.level_label_image = self.font.render(level_str, True, self.text_color, self.aa_game.settings.bg_color)

        # Display the level at top right below score
        self.level_label_rect = self.level_label_image.get_rect()
        self.level_label_rect.right = self.score_label_rect.right
        self.level_label_rect.top = 10 + self.score_label_rect.bottom


    def update_remaining_ships(self):
        """Show how many ships(lives) are left"""
        self.ships = Group()
        for ship_number in range(self.aa_game.game_stats.ships_remaining):
            ship = Ship(self.aa_game)
            ship.rect.x = 10 + ship.rect.width * ship_number
            ship.rect.y = 10
            self.ships.add(ship)


    def draw(self):
        """Drawing Scores, level number and remaining ships to the game screen"""
        self.aa_game.screen.blit(self.score_label_image, self.score_label_rect)
        self.aa_game.screen.blit(self.high_score_label_image, self.high_score_label_rect)
        self.aa_game.screen.blit(self.level_label_image, self.level_label_rect)
        self.ships.draw(self.aa_game.screen)

