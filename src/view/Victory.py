import pygame

from src.constant import COLOR_WHITE, COLOR_BLACK, START_GAME
from src.constant import GAME_FONT
from src.constant import GAME_SOUND
from src.constant import START_BACKGROUND_IMG
from src.constant import WIDTH, HEIGTH


# noinspection PyMethodMayBeStatic
class Victory:

    def __init__(self, title, screen):
        self.mouse_position = pygame.mouse.get_pos()
        self.menu_font = pygame.font.Font(GAME_FONT, 60)
        self.surface_screen = screen
        self.surface_screen.blit(pygame.image.load(START_BACKGROUND_IMG).convert(), [0, 0])
        self.text_screen = ''
        self.text_rect = ''

    def victory(self, victory_name=''):
        """Define winner game name on start screen"""
        text = ''
        for char in victory_name:
            text += char
            self.text_screen = self.menu_font.render(text, True, COLOR_WHITE, COLOR_BLACK)
            text_rect = self.text_screen.get_rect()
            text_rect.center = (WIDTH/2, (HEIGTH/2)-200)
            self.surface_screen.blit(self.text_screen, text_rect)
            pygame.display.update()
            pygame.time.wait(300)

        text = ''
        for char in 'Winner':
            text += char
            self.text_screen = self.menu_font.render(text, True, COLOR_WHITE, COLOR_BLACK)
            text_rect = self.text_screen.get_rect()
            text_rect.center = (WIDTH/2, (HEIGTH/2)-100)
            self.surface_screen.blit(self.text_screen, text_rect)
            pygame.display.update()
            pygame.time.wait(300)

