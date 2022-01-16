import pygame.font


class Scoreboard():
    """Класс для вывода игровой информации."""

    def __init__(self, ai_game):
        """Инициализирует атрибуты подсчета очков."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Настройка шрифта
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        # Подготовка исходного изображения
        self.prep_score()
        self.prep_high_score()
        self.prep_exit_text()
        self.prep_level()

    def prep_score(self):
        """Преобразует текущий счет в графическое изображение."""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score).replace(',', ' ')
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Вывод счета в правой верхней части экрана
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Преобразует рекордный счет в графическое изображение."""
        rounded_high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(rounded_high_score).replace(',', ' ')
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        # Вывод счета по центру в верхней части экрана
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_exit_text(self):
        """Готовит информационный текст о способе выхода из игры."""
        exit_text_str = "Q - exit"
        self.exit_text_image = self.font.render(exit_text_str, True, self.text_color, self.settings.bg_color)

        # Вывод в левой верхней части экрана
        self.exit_text_rect = self.exit_text_image.get_rect()
        self.exit_text_rect.left = self.screen_rect.left + 20
        self.exit_text_rect.top = self.score_rect.top

    def prep_level(self):
        """Преобразует текущий уровень в графическое изображение."""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        # Вывод под счетом
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def show_score(self):
        """Выводит счет на экран."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.exit_text_image, self.exit_text_rect)
        self.screen.blit(self.level_image, self.level_rect)

    def check_high_score(self):
        """Проверяет появление рекорда."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
