class Settings:
    """A Class to store all settings"""

    def __init__(self):
        """Game's initial settings"""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.delay = 0.75

        # Ship
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 20
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 7

        # Alien settings
        self.alien_fleet_drop_speed = 10

        # How quickly the game speeds up after winning each level
        self.speedup_scale = 1.1

        # How quickly the alien killing score increase after winning each level
        self.score_increase_scale = 1.5

        self.init_dynamic_settings()


    def init_dynamic_settings(self):
        """Initialize settings that change at each level of the game"""
        self.ship_speed = 0.5
        self.bullet_speed = 2.0
        self.alien_horizontal_speed = 0.5
        # -1 represent fleet moving to left, +1 means it moves to right
        self.alien_fleet_direction = 1
        # Scoring
        self.alien_killing_score = 7


    def level_up(self):
        """Increase game speed and score as leveling up"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_horizontal_speed *= self.speedup_scale

        self.alien_killing_score = int(self.alien_killing_score * self.score_increase_scale)
        # print('Leveled up ', self.ship_speed, ' ', self.bullet_speed , ' ', self.alien_horizontal_speed, ' ', self.alien_killing_score)
