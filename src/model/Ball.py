import pygame

from src.constant import WIDTH, HEIGTH, BOUNCE_SOUND, POINT_SOUND


# noinspection DuplicatedCode,PyMethodMayBeStatic
class Ball:
    def __init__(self, x=(WIDTH / 2 - 15), y=(HEIGTH / 2 - 15)):
        self.obj = pygame.Rect(x, y, 30, 30)
        self.speed_x = 7
        self.speed_y = 7
        self.score_1 = 0
        self.score_2 = 0

    def movement(self):
        """This function will be update position of the per frame a and call
        all functions related with the position of the like the collision with
        wall"""
        self.obj.x += self.speed_x
        self.obj.y += self.speed_y
        self.wall_collision()
        self.reset_ball()

    def wall_collision(self):
        """Check collision with wall"""
        # if 340 < self.obj.x < 950 and 60 < self.obj.y < HEIGTH - 60:
        if self.obj.top <= 60 or self.obj.bottom >= HEIGTH - 60:
            self.speed_y *= -1
            self.play_sound(BOUNCE_SOUND)
        if self.obj.left <= 79 or self.obj.right >= WIDTH-69:
            self.speed_x *= -1
            self.play_sound(POINT_SOUND)
            if self.obj.left <= 79:
                self.score_1 += 1
            if self.obj.right >= WIDTH-69:
                self.score_2 += 1

    def player_collider(self, player, opponent):
        """Check collision with player and opponent ai"""
        if self.obj.colliderect(player):
            if abs(self.obj.right - player.left) < 10:
                self.speed_x *= -1
                self.play_sound(BOUNCE_SOUND)
            elif abs(self.obj.bottom - player.top) < 10 and self.speed_y > 0:
                self.speed_y *= -1
                self.play_sound(BOUNCE_SOUND)
            elif abs(self.obj.top - player.bottom) < 10 and self.speed_y < 0:
                self.speed_y *= -1
                self.play_sound(BOUNCE_SOUND)

        if self.obj.colliderect(opponent):
            if abs(self.obj.left - opponent.right) < 10:
                self.speed_x *= -1
                self.play_sound(BOUNCE_SOUND)
            elif abs(self.obj.bottom - opponent.top) < 10 and self.speed_y > 0:
                self.speed_y *= -1
                self.play_sound(BOUNCE_SOUND)
            elif abs(self.obj.top - opponent.bottom) < 10 and self.speed_y < 0:
                self.speed_y *= -1
                self.play_sound(BOUNCE_SOUND)

    def reset_ball(self):
        """Reset ball"""
        if self.obj.left <= 80 or self.obj.right >= WIDTH - 70:
            self.obj.center = (WIDTH / 2, HEIGTH / 2)

    def play_sound(self, sound_name):
        obj = pygame.mixer.Sound(sound_name)
        obj.play()

