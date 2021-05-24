import pygame
import sys

from src.constant import SCREEN_SIZE, COLOR_BLACK, COLOR_WHITE, GAME_BACKGROUND, INIT_GAME, GAME_FONT, WIDTH, HEIGTH, \
    MAX_SCORE
from src.model.Ball import Ball
from src.model.Opponent import Opponent
from src.model.Player import Player
from src.view import StartScreen, Victory


# noinspection PyMethodMayBeStatic,PyAttributeOutsideInit
class ControlMain:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.running = True
        self.score_1 = 0
        self.score_2 = 0
        self.on_start_screen = True
        self.on_game_screen = False
        self.on_victory_screen = False
        self.ball = Ball()
        self.player = Player()
        self.opponent = Opponent()
        self.victory = Victory('Victory', self.screen)

    def create_start_screen(self):
        """Create start screen"""
        self.start_screen = StartScreen('Pong', self.screen)
        self.start_screen.play_sound()
        self.start_screen.game_name()

    def listen_options_start_screen(self):
        """Listen events on start screen"""
        self.start_screen.start_button()
        self.start_screen.quit_button()

    def __quit_game(self, event):
        """Quit game"""
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    def playing_game(self):
        self.screen.fill(COLOR_BLACK)
        self.screen.blit(pygame.image.load(GAME_BACKGROUND).convert(), [0, 0])
        self.ball.movement()
        self.ball.player_collider(self.player.obj, self.opponent.obj)
        self.player.movement()
        self.opponent.movement(self.ball.obj)
        pygame.draw.ellipse(self.screen, COLOR_WHITE, self.ball.obj)
        pygame.draw.rect(self.screen, COLOR_WHITE, self.player.obj)
        pygame.draw.rect(self.screen, COLOR_WHITE, self.opponent.obj)

    def handle_events(self):
        for event in pygame.event.get():
            # Listen player controls
            self.player.control_speed(event)
            # Start game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.on_start_screen:
                    self.start_screen.start_key_event()
                    self.on_start_screen = False
                    self.on_game_screen = True
                    obj = pygame.mixer.Sound(INIT_GAME)
                    obj.play()

            # Quit game
            self.__quit_game(event)

    def main(self):
        """Main Function Game"""
        pygame.display.set_caption("MyPong - PyGame Edition - 2021.05.18")
        self.create_start_screen()

        while self.running:

            # Events to game
            self.handle_events()

            # Just check is on start screen
            if self.on_start_screen:
                self.listen_options_start_screen()

            # Playing game
            if self.on_game_screen:
                self.playing_game()
                self.handle_score()

            pygame.display.update()
        pygame.quit()

    def handle_score(self):
        self.score_1 = self.ball.score_1
        self.score_2 = self.ball.score_2
        quit_font = pygame.font.Font(GAME_FONT, 25)
        scores_msg = f'{self.score_2} x {self.score_1}'
        quit_text = quit_font.render(scores_msg, True, COLOR_WHITE, COLOR_BLACK)
        quit_rect = quit_text.get_rect()
        quit_rect.center = (WIDTH / 2, 20)
        self.screen.blit(quit_text, quit_rect)

        if self.score_1 == MAX_SCORE or self.score_2 == MAX_SCORE:
            self.screen.fill(COLOR_BLACK)
            self.on_game_screen = False
            self.on_victory_screen = True
            self.screen.blit(pygame.image.load(GAME_BACKGROUND).convert(), [0, 0])

        if self.on_victory_screen:
            if self.score_1 == MAX_SCORE:
                self.victory.victory('Player 1')
            if self.score_2 == MAX_SCORE:
                self.victory.victory('Player 2')


if __name__ == '__main__':
    c = ControlMain()
    c.main()
