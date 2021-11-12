import pygame

class Ship():
    """Класс управления кораблем."""

    def __init__(self, ai_game):
        """Инициализирует корабль, задает его начальную позицию."""

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Загружает изображение, получает прямоугольник
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Новый корабль появляется у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom
        # Сохранение вещественной координаты
        self.x = float(self.rect.x)

        # Флаги перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        if self.moving_right:
            # self.rect.x += self.settings.ship_speed
            self.x += self.settings.ship_speed
        if self.moving_left:
            # self.rect.x -= self.settings.ship_speed
            self.x -= self.settings.ship_speed

        # Обновление атрибута rect на основании self.x
        self.rect.x = self.x

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)