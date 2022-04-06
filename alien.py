import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """The main class for aliens controlling"""

    def __init__(self, ai_game):
        """Aliens fleet's settings"""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.right = self.screen_rect.right

        self.x = float(self.rect.x)

    def update(self):
        """This method update alien's vertical position"""
        # self.x -= self.settings.alien_speed
        # self.rect.x = self.x

        # old version
        # self.x -= self.settings.alien_speed
        self.rect.x -= self.settings.alien_speed
