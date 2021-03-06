class Settings():
    """Класс для хранения всех настроек игры Alien Invision"""

    def __init__(self):
        """Инициализирует настройки игры."""

        # Параметры экрана
        self.fullscreen_mode = True
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (0, 2, 54)

        # Настройки корабля
        self.ship_limit = 3

        # Параметры снарядов
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (217, 33, 33)
        self.bullet_allowed = 3

        # Настройки пришельцев
        self.fleet_drop_speed = 10

        # Темп ускорения игры
        self.speedup_scale = 1.5
        # Темп увеличения стоимости пришельцев
        self.score_scale = self.speedup_scale

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, меняющиеся в игре."""
        self.ship_speed = 8.5
        self.bullet_speed = 15.5
        self.alien_speed = 1.0
        self.fleet_direction = 1  # направление движения право/лево - 1/-1
        self.alien_points = 50

    def increase_speed(self):
        """Увеличивает скорости."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
