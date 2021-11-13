import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Класс одного пришельца."""

    def __init__(self, ai_game):
        """Инициирует пришельца, задает начальную позицию."""

        super().__init__()
        self.screen = ai_game.screen

        # Загрузка изображения пришельца и назначение атрибута rect
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        # Пришелец появляется в левом верхнем углу с отступом на размер корабля пришельцев
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Точная позиция пришельца по горизонтали (для регулирования скорости)
        self.x = float(self.rect.x)

