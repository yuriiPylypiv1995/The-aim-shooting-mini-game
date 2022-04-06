class Settings:
    """This is a class for saving all of game's settings"""
    def __init__(self):
        """Game settings initialization"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 670
        self.bg_color = (230, 230, 230)

        # The ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullets settings
        self.bullet_speed = 1.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

        # Aliens settings
        self.alien_speed = 1.0
        self.alien_additional_x = 1300