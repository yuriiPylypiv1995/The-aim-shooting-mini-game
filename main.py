# tasks 14_2

import sys
import pygame

from time import sleep
from settings import Settings
from ship import Ship
from bullet import Bullet
from game_stats import GameStats
from rectangle import Rectangle
from button import Button

class AlienInvasion:
    """Class for game initialization"""

    def __init__(self):
        """Game initialization"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()

        pygame.display.set_caption("The aim shooting")

        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.aim = Rectangle(self)
        self.bullets = pygame.sprite.Group()
        self.play_button = Button(self, 'Play')

    def run_game(self):
        """The main cycle of the game"""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update_position()
                self._update_bullets()
                self._check_aim_edges()
                self.aim.update()
            self._update_screen()

    def _check_events(self):
        # The events monitoring
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start the game when a user clicked the play button"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.stats.reset_stats()
            self.stats.game_active = True
            self.bullets.empty()
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """Reaction on pressing buttons"""
        if event.key == pygame.K_DOWN:
            # Replace the spaceship on 1 pix right
            self.ship.moving_down = True
        elif event.key == pygame.K_UP:
            # Replace the spaceship on 1 pix left
            self.ship.moving_up = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_F12:
            # Open the game in the fullscreen mode
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
            self.ship.rect.y += 100
            self.ship.screen_rect.right += 168
        elif event.key == pygame.K_ESCAPE:
            # Exit from the fullscreen mode
            self.screen = pygame.display.set_mode((1200, 670))
            if self.ship.x < 0:
                self.ship.x = 0
            elif self.ship.x > 1200:
                self.ship.x -= 168
            self.ship.rect.y -= 100
            self.ship.screen_rect.right -= 168

    def _check_keyup_events(self, event):
        """Reaction wnen a button is not pressed"""
        if event.key == pygame.K_DOWN:
            # Do not move the spaceship
            self.ship.moving_down = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False

    def _update_screen(self):
        # Repainting the screen after each cycle iteration
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aim.draw_aim()
        if not self.stats.game_active:
            self.play_button.draw_button()

        # Show the last painted screen
        pygame.display.flip()

    def _fire_bullet(self):
        # Adding new bullet to group
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """The method for bullets updating"""
        # Bullets positions updating
        self.bullets.update()
        # Removing bullets that out of the screen
        for bullet in self.bullets.copy():
            if bullet.rect.left > self.ship.screen_rect.right:
                self.bullets.remove(bullet)
        if pygame.sprite.spritecollideany(self.aim, self.bullets):
            self.bullets.empty()
            self.settings.aimed_patrons += 1
            print(self.settings.aimed_patrons)
            if self.settings.aimed_patrons >= 5:
                self.stats.game_active = False
                print("You have won!")
                pygame.mouse.set_visible(True)
        else:
            self._lost_patron_counter()

    def _lost_patron_counter(self):
        """The method is a counter of all lost patrons during the game"""
        for bullet in self.bullets.sprites():
            if bullet.rect.left >= self.screen_rect.right:
                self.settings.lost_patrons += 1
                print(self.settings.lost_patrons)
        if self.settings.lost_patrons >= 3:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
            print("Game is over. You have lost")

    def _ship_hit(self):
        """This method regulates game's behavior when the fleet touched the ship"""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.bullets.empty()
            sleep(0.5)
        else:
            self.stats.game_active = False

    def _check_aim_edges(self):
        """Check if the aim reached the buttom of the screen"""
        if self.aim.check_edges():
            self._change_aim_direction()

    def _change_aim_direction(self):
        """Change the aim direction to up"""
        self.aim.y -= self.settings.aim_up_speed
        self.settings.changer_direction *= -1

if __name__ == "__main__":
    # Creating the game object and run the game
    ai = AlienInvasion()
    ai.run_game()
