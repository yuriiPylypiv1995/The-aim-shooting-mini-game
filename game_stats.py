class GameStats:
    """This method for game statistic moderating"""

    def __init__(self, ai_game):
        """Statistic initialization"""
        self.ships_left = None
        self.settings = ai_game.settings
        self.reset_stats()

        # Start the game with inactive state
        self.game_active = False

    def reset_stats(self):
        """This statistic can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.settings.aimed_patrons = 0
        self.settings.lost_patrons = 0
