import pygame

from src.constant import WIDTH, HEIGTH


class Player:
    def __init__(self):
        self.obj = pygame.Rect((WIDTH - 90), (HEIGTH / 2 - 70), 20, 140)
        self.speed = 0

    def control_speed(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.speed += 7
            if event.key == pygame.K_UP:
                self.speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                self.speed -= 7
            if event.key == pygame.K_UP:
                self.speed += 7

    def movement(self):
        self.obj.y += self.speed
        if self.obj.top <= 0:
            self.obj.top = 0
        if self.obj.bottom >= HEIGTH:
            self.obj.bottom = HEIGTH
