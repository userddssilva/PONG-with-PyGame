import pygame

from src.constant import HEIGTH


class Opponent:
    def __init__(self):
        self.obj = pygame.Rect(76, (HEIGTH / 2 - 70), 20, 140)
        self.speed = 9

    def movement(self, ball):
        if self.obj.top < ball.y:
            self.obj.top += self.speed
        if self.obj.bottom > ball.y:
            self.obj.bottom -= self.speed
        if self.obj.top <= 0:
            self.obj.top = 0
        if self.obj.bottom >= HEIGTH:
            self.obj.bottom = HEIGTH
