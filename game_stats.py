class GameStats():
    """Отслеживание статистики для Alien Invision."""

    def __init__(self, ai_game):
        """Инициирует статистику."""
        self.settings = ai_game.settings
        self.game_active = False
        self.reset_stats()

    def reset_stats(self):
        """Инициализирует статистику, меняющуюся в ходе игры."""
        self.ships_left = self.settings.ship_limit