class GameStats:
    """Tracking player statistics for the game!"""

    def __init__(self, aa_game):
        self.game_settings = aa_game.settings
        self.ships_remaining = 0
        self.game_active = False
        self.score = 0
        self.high_score = 0
        self.level = 1


    def reset(self):
        self.ships_remaining = self.game_settings.ship_limit
        self.game_active = True
        self.score = 0
        self.level = 1


    def lost_a_game(self):
        self.ships_remaining -= 1
        if self.ships_remaining == 0:
            self.game_active = False


    def is_game_active(self):
        return self.game_active


    def level_up(self):
        self.level += 1

