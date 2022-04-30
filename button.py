import pygame.font

class Button:
    """This is a class for game buttons creation"""

    def __init__(self, o_k_game, msg):
        """The button's attributes initialization"""
        self.screen = o_k_game.screen
        self.screen_rect = self.screen.get_rect()

        # The size and button's properties
        self.width, self.height = 200, 50
        self.button_color = (100, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # The Rect object creation and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # About the message on the button
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Change text to an image and center it on the screen"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """The method for buttons drawing"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)