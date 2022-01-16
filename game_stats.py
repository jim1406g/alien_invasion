class GameStats():
    """Отслеживание статистики для Alien Invision."""

    def __init__(self, ai_game):
        """Инициирует статистику."""
        self.settings = ai_game.settings
        self.game_active = False
        self.reset_stats()
        # Рекорд
        self.high_score = 0

    def reset_stats(self):
        """Инициализирует статистику, меняющуюся в ходе игры."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
