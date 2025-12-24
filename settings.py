class Settings:
    """A Class to store all settings"""

    def __init__(self):
        """Game's initial settings"""

        # Screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 0.5

        # Bullet
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_speed = 0.25
        self.bullet_allowed = 3