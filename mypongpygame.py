import random
import pygame
pygame.init()

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

# display Config
SCORE_MAX = 5
size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("MyPong - PyGame Edition - 2021.05.18")

# score text
score_font = pygame.font.Font('assets/PressStart2P.ttf', 44)
score_text = score_font.render('00 x 00', True, COLOR_WHITE, COLOR_BLACK)
score_text_rect = score_text.get_rect()
score_text_rect.center = (680, 50)

# victory text
victory_font = pygame.font.Font('assets/PressStart2P.ttf', 100)
victory_text = victory_font .render('VICTORY', True, COLOR_WHITE, COLOR_BLACK)
victory_text_rect = score_text.get_rect()
victory_text_rect.center = (450, 350)

# Menu text
menu_font = pygame.font.Font('assets/PressStart2P.ttf', 60)
menu_text = menu_font .render('Press SPACE', True, COLOR_WHITE, COLOR_BLACK)
menu_text_rect = score_text.get_rect()
menu_text_rect.center = (450, 350)


# sound effects
bounce_sound_effect = pygame.mixer.Sound('assets/bounce.wav')
scoring_sound_effect = pygame.mixer.Sound('assets/point.wav')
buff_sound_effect = pygame.mixer.Sound('assets/coin.wav')
nerf_sound_effect = pygame.mixer.Sound('assets/loose.wav')

# player 1
player_1 = pygame.image.load("assets/player.png")
player_1_y = 300
player_1_move_up = False
player_1_move_down = False
player_1_size = 150

# player 2 - robot
player_2 = pygame.image.load("assets/player.png")
player_2_y = 300
player_2_size = 150

# Lucky Block
spawn_locked = True
last_touch = 0
lucky_block = pygame.image.load("assets/lucky_block.gif")
lucky_block_x = 0
lucky_block_y = 0
buff_timer_player1 = 0
buff_timer_player2 = 0
nerf_timer_player1 = 0
nerf_timer_player2 = 0

# ball
ball = pygame.image.load("assets/ball.png")
ball_x = 640
ball_y = 360
ball_dx = 5
ball_dy = 5

# score
score_1 = 0
score_2 = 0

# game loop
game_loop = True
game_pause = True
game_clock = pygame.time.Clock()


# End Buff
def end_buff(num_paddle):
    global player_1_size
    global player_2_size
    if num_paddle == 1:
        player_1_size = 150
    else:
        # Change sprite
        player_2_size = 150
    return pygame.image.load("assets/player.png")


while game_loop:

    # lucky_Block Spawn
    buffTry = random.randint(0, 800)
    if buffTry == 150 and spawn_locked and not (last_touch == 0):
        # Select the buff
        buffX = random.randint(200, 1080)
        buffY = random.randint(100, 620)
        lucky_block_x = buffX
        lucky_block_y = buffY
        spawn_locked = False

    # timer buff paddle 1
    buff_timer_player1 -= 0.0009
    if buff_timer_player1 < 0:
        buff_timer_player1 = 1
        player_1 = end_buff(1)

    # timer buff paddle 2
    buff_timer_player2 -= 0.0009
    if buff_timer_player2 < 0:
        buff_timer_player2 = 1
        player_2 = end_buff(2)

    # time nerf paddle 1
    nerf_timer_player1 -= 0.0009
    if nerf_timer_player1 < 0:
        nerf_timer_player1 = 1
        player_1 = end_buff(1)

    # timer nerf paddle 2
    nerf_timer_player2 -= 0.0009
    if nerf_timer_player2 < 0:
        nerf_timer_player2 = 1
        player_2 = end_buff(2)

    # Movement
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

        #  keystroke events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_1_move_up = True
            if event.key == pygame.K_DOWN:
                player_1_move_down = True
            if event.key == pygame.K_SPACE:
                game_pause = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_1_move_up = False
            if event.key == pygame.K_DOWN:
                player_1_move_down = False

    # checking the victory condition
    if score_1 < SCORE_MAX and score_2 < SCORE_MAX:

        # clear screen
        screen.fill(COLOR_BLACK)

        # ball collision with the wall
        if ball_y > 700:
            ball_dy *= -1.0009
            bounce_sound_effect.play()
        elif ball_y <= 0:
            ball_dy *= -1.0009
            bounce_sound_effect.play()

        # collision with buff
        if (ball_x + 40 >= lucky_block_x >= ball_x - 40) and \
                (ball_y + 40 >= lucky_block_y >= ball_y - 40):
            spawn_locked = True
            lucky_block_x = -110
            lucky_block_y = -110
            rand_buff = random.randint(0, 1)
            if rand_buff == 0 or rand_buff == 1:
                if rand_buff == 0:
                    buff_sound_effect.play()
                    if last_touch == 1:
                        player_1_size = 200
                        player_1 = pygame.image.load("assets/player_buff.png")
                        buff_timer_player1 = 30
                    else:
                        player_2_size = 200
                        player_2 = pygame.image.load("assets/player_buff.png")
                        buff_timer_player2 = 30

                else:
                    nerf_sound_effect.play()
                    if last_touch == 1:
                        player_1_size = 90
                        player_1 = pygame.image.load("assets/player_nerf.png")
                        nerf_timer_player1 = 30
                    else:
                        player_2_size = 90
                        player_2 = pygame.image.load("assets/player_nerf.png")
                        nerf_timer_player2 = 30

        # ball collision with the player 1 's paddle
        if ball_x < 100 and not (ball_x < 80):
            if player_1_y < ball_y + 25:
                if player_1_y + player_1_size > ball_y:
                    ball_x = 102
                    ball_dx *= -1.1
                    bounce_sound_effect.play()
                    last_touch = 1

        # ball collision with the player 2 's paddle
        if (ball_x > 1160) and not (ball_x > 1190):
            if player_2_y < ball_y + 25:
                if player_2_y + player_2_size > ball_y:
                    ball_dx *= -1.1
                    ball_x = 1158
                    last_touch = 2

            bounce_sound_effect.play()

        if ball_dx >= 20:
            ball_dx = 20
        elif ball_dx <= -20:
            ball_dx = -20

        # scoring points
        if ball_x < -50:
            if ball_dx < 5:
                ball_dx = -5
            else:
                ball_dx = 5
            ball_x = 640
            ball_y = 360
            ball_dy *= -1
            ball_dx *= -1
            score_2 += 1
            scoring_sound_effect.play()
        elif ball_x > 1320:
            if ball_dx < 5:
                ball_dx = -5
            else:
                ball_dx = 5
            ball_x = 640
            ball_y = 360
            ball_dy *= -1
            ball_dx *= -1
            score_1 += 1
            scoring_sound_effect.play()

        if not game_pause:
            # ball movement
            ball_x = ball_x + ball_dx
            ball_y = ball_y + ball_dy

            # player 1 up movement
            if player_1_move_up:
                player_1_y -= 5
            else:
                player_1_y += 0

            # player 1 down movement
            if player_1_move_down:
                player_1_y += 5
            else:
                player_1_y += 0

            # player 2 "Artificial Intelligence"
            if player_2_y > ball_y:
                player_2_y -= 4.8
            elif player_2_y < ball_y:
                player_2_y += 4.8

            # player 1 collides with upper wall
            if player_1_y <= 0:
                player_1_y = 0

            # player 1 collides with lower wall
            elif player_1_y >= 720 - player_1_size :
                player_1_y = 720 - player_1_size

            # Player 2 collides with lower wall
            if player_2_y <= 0:
                player_2_y = 0

            # player 2 collides with lower wall
            elif player_2_y >= 720 - player_2_size:
                player_2_y = 720 - player_2_size

            # update score hud
            score_text = score_font.render(str(score_1) + ' x ' + str(score_2), True, COLOR_WHITE, COLOR_BLACK)

            # drawing objects
            screen.blit(score_text, score_text_rect)
            screen.blit(ball, (ball_x, ball_y))
            screen.blit(player_1, (80, player_1_y))
            screen.blit(player_2, (1180, player_2_y))
            if not spawn_locked:
                screen.blit(lucky_block, (lucky_block_x, lucky_block_y))

        else:
            screen.fill(COLOR_BLACK)
            screen.blit(menu_text, menu_text_rect)

    else:
        # drawing victory
        screen.fill(COLOR_BLACK)
        screen.blit(score_text, score_text_rect)
        screen.blit(victory_text, victory_text_rect)

    # update screen
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()
