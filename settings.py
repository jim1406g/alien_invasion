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
        self.ship_speed = 8.5

        # Параметры снарядов
        self.bullet_speed = 15.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (217, 33, 33)
        self.bullet_allowed = 3

        # Настройки пришельцев
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # направление движения право/лево - 1/-1
