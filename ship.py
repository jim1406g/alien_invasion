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

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)