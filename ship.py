import pygame

class Ship():
    """Класс управления кораблем."""

    def __init__(self, ai_game):
        """Инициализирует корабль, задает его начальную позицию."""

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Загружает изображение, получает прямоугольник
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Новый корабль появляется у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom

        # Флаги перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)