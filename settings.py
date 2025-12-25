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
        self.ship_speed = 0.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 20
        self.bullet_color = (60, 60, 60)
        self.bullet_speed = 2.0
        self.bullet_allowed = 7

        # Alien settings
        self.alien_horizontal_speed = 0.5
        self.alien_fleet_drop_speed = 10
        # -1 represent fleet moving to left, +1 means it moves to right
        self.alien_fleet_direction = 1
