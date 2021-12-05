import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Класс одного пришельца."""

    def __init__(self, ai_game):
        """Инициирует пришельца, задает начальную позицию."""

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Загрузка изображения пришельца и назначение атрибута rect
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        # Пришелец появляется в левом верхнем углу с отступом на размер корабля пришельцев
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Точная позиция пришельца по горизонтали (для регулирования скорости)
        self.x = float(self.rect.x)

    def check_edges(self):
        """Возвращает True, если пришелец у края экрана"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Перемещает пришельца вправо."""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
