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
        self.bullets_allowed = 5

        # Aims settings
        self.aim_width = 200
        self.aim_height = 170
        self.aim_background = (255, 0, 0)
        self.aim_speed_y = 0.1
        self.changer_direction = 1
        self.aim_up_speed = 1
        self.aimed_patrons = 0
        self.lost_patrons = 0

        # The settings increaser
        self.speed_increse = 0.0001

    def default_speed_settings(self):
        """The dynamic speed settings initialization"""
        self.ship_speed = 1.5
        self.bullet_speed = 1.0
        self.aim_speed_y = 0.1

    def speed_increser(self):
        """This is a method for speed settings increase"""
        self.bullet_speed += self.speed_increse
        if self.aim_speed_y < 2.0:
            self.aim_speed_y += self.speed_increse
        else:
            self.aim_speed_y = 2.0
