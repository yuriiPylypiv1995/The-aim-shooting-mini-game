import pygame

class Rectangle:
    """This is a class for aim's creation"""

    def __init__(self, o_k_game):
        """Aim's settings"""
        self.screen = o_k_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = o_k_game.settings
        self.rect = pygame.Rect(0, 0, self.settings.aim_width, self.settings.aim_height)
        self.rect.x = 900
        self.rect.y = 10
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        """The method for aim's positin updating (moving)"""
        self.y += (self.settings.aim_speed_y * self.settings.changer_direction)
        self.rect.y = self.y

    def draw_aim(self):
        """This method draw the aims"""
        self.screen.fill(self.settings.aim_background, self.rect)

    def check_edges(self):
        """This method check if an aim reached the button of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top == screen_rect.top and \
                self.settings.changer_direction == -1:
            return True

