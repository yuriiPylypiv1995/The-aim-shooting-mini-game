import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """The class for bullet control"""

    def __init__(self, ai_game):
        """Bullet settings"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midright = ai_game.ship.rect.midright

        self.x = float(self.rect.x)

    def update(self):
        """This method update bullet vertical position"""
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        """This method draw bullets with their parameters and color"""
        pygame.draw.rect(self.screen, self.color, self.rect)