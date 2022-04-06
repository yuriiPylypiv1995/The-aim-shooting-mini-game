class GameStats:
    """This method for game statistic moderating"""

    def __init__(self, ai_game):
        """Statistic initialization"""
        self.dead_aliens = None
        self.ships_left = None
        self.settings = ai_game.settings
        self.reset_stats()

        # Start the game with active state
        self.game_active = True

    def reset_stats(self):
        """This statistic can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.dead_aliens = 0
