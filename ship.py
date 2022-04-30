import pygame

class Ship:
    """The spaceship params and working"""

    def __init__(self, ai_game):
        """The spaceship initialization and start position"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings

        # Getting an image of the spaceship
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Setting of the spaceship start position (on the botton centre of the screen)
        self.rect.bottomleft = self.screen_rect.bottomleft

        self.y = float(self.rect.y)

        # The moving right indicator
        self.moving_down = False
        # The moving left indicator
        self.moving_up = False

    def update_position(self):
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed

        # Updating rect y
        self.rect.y = self.y

    def blitme(self):
        """Paiting of the spaceship on its start position"""
        self.screen.blit(self.image, self.rect)