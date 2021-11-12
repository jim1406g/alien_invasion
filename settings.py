class Settings():
    """Класс для хранения всех настроек игры Alien Invision"""

    def __init__(self):
        """Инициализирует настройки игры."""

        # Параметры экрана
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (0, 2, 54)

        # Настройки корабля
        self.ship_speed = 1.5
