import pygame

from src.constant import COLOR_WHITE, COLOR_BLACK, START_GAME
from src.constant import GAME_FONT
from src.constant import GAME_SOUND
from src.constant import START_BACKGROUND_IMG
from src.constant import WIDTH, HEIGTH


# noinspection PyMethodMayBeStatic
class StartScreen:
    width = WIDTH
    heigth = HEIGTH
    running = True
    screen = pygame.display
    events = pygame.event
    font = pygame.font
    sound = pygame.mixer
    size_start_text = 0

    def __init__(self, title, screen):
        self.mouse_position = pygame.mouse.get_pos()
        self.menu_font = self.font.Font(GAME_FONT, 60)
        self.surface_screen = screen
        self.surface_screen.blit(pygame.image.load(START_BACKGROUND_IMG).convert(), [0, 0])
        self.screen.set_caption(title)
        self.text_screen = ''
        self.text_rect = ''

    def update(self):
        """Update screen"""
        self.screen.update()

    def start_key_event(self):
        """Function to start the game"""
        self.sound.music.stop()
        obj = pygame.mixer.Sound(START_GAME)
        obj.play()
        self.surface_screen.fill(COLOR_BLACK)
        self.update()
        pygame.time.wait(1000)
        # return False

    def game_name(self):
        """Define game name on start screen"""
        text = ''
        for char in 'PONG!':
            text += char
            self.text_screen = self.menu_font.render(text, True, COLOR_WHITE, COLOR_BLACK)
            text_rect = self.text_screen.get_rect()
            text_rect.center = (self.width/2, (self.heigth/2)-200)
            self.surface_screen.blit(self.text_screen, text_rect)
            self.update()
            pygame.time.wait(300)

        text = ''
        for char in 'With PyGame':
            text += char
            self.text_screen = self.menu_font.render(text, True, COLOR_WHITE, COLOR_BLACK)
            text_rect = self.text_screen.get_rect()
            text_rect.center = (self.width/2, (self.heigth/2)-100)
            self.surface_screen.blit(self.text_screen, text_rect)
            self.update()
            pygame.time.wait(300)

    def start_button(self):
        """Config start button"""
        if self.size_start_text == 1:
            self.size_start_text = 0
            start_font = self.font.Font(GAME_FONT, 18)
        else:
            self.size_start_text = 1
            start_font = self.font.Font(GAME_FONT, 21)
        start_text = start_font.render('Press SPACE to Start', True, COLOR_WHITE, COLOR_BLACK)
        start_rect = start_text.get_rect()
        start_rect.center = (self.width/2, (self.heigth/2))
        self.surface_screen.blit(start_text, start_rect)
        self.update()
        start_text = start_font.render('Press SPACE to Start', True, COLOR_BLACK)
        self.surface_screen.blit(start_text, start_rect)
        pygame.time.wait(500)

    def quit_button(self):
        """Config quit button"""
        quit_font = self.font.Font(GAME_FONT, 25)
        quit_text = quit_font.render('Quit Game (ESC)', True, COLOR_WHITE, COLOR_BLACK)
        quit_rect = quit_text.get_rect()
        quit_rect.center = (self.width/2, self.heigth-70)
        self.surface_screen.blit(quit_text, quit_rect)

    def play_sound(self):
        """Play sound on the background"""
        self.sound.music.load(GAME_SOUND)
        # play the music infinite
        self.sound.music.play(-1)
