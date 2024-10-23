import pygame

pygame.init()
screen_width = 800
screen_height = 600
x = 350
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong by MatiKa211")
FPS = 60
clock = pygame.time.Clock()
max_speed = 8

My_paddle = pygame.Rect(x, 497.5, 110, 5)
Opponent_paddle = pygame.Rect(x, 97.5, 110, 5)
ball_speed_x = 2
ball_speed_y = 2
ball = pygame.Rect(397.5, 297.5, 10, 10)
score1 = 0
score2 = 0
font = pygame.font.Font(None, 36)

current_speed_x = ball_speed_x
current_speed_y = ball_speed_y

def move_ball():
    global current_speed_x, current_speed_y, score1, score2

    ball.x += current_speed_x
    ball.y += current_speed_y

    if ball.colliderect(My_paddle) or ball.colliderect(Opponent_paddle):
        current_speed_y *= -1
        if abs(current_speed_x) < max_speed:
            current_speed_x *= 1.0001
        if abs(current_speed_y) < max_speed:
            current_speed_y *= 1.0001

    if ball.left <= 0 or ball.right >= screen_width:
        current_speed_x *= -1

    if ball.top <= 0:
        score1 += 1
        reset_ball()
        countdown()
        reset_paddles()  # Resetuj pozycje paletek

    if ball.bottom >= screen_height:
        score2 += 1
        reset_ball()
        countdown()
        reset_paddles()  # Resetuj pozycje paletek

def reset_ball():
    global current_speed_x, current_speed_y
    ball.center = (screen_width // 2, screen_height // 2)
    current_speed_x = ball_speed_x
    current_speed_y = ball_speed_y
    current_speed_y *= -1

def reset_paddles():
    My_paddle.x = x  # Resetuj paletkę gracza
    Opponent_paddle.x = x  # Resetuj paletkę przeciwnika

def countdown():
    for i in range(3, 0, -1):
        screen.fill((0, 0, 0))
        text = font.render(str(i), True, (255, 255, 255))
        screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))
        pygame.display.flip()
        pygame.time.delay(1000)

text = font.render("Naciśnij Enter, aby rozpocząć", True, (255, 255, 255))
screen.blit(text, (200, 300))

pygame.display.flip()

waiting = True
while waiting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            waiting = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                waiting = False

running = True
while running:
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 255, 255), My_paddle)
    pygame.draw.rect(screen, (255, 255, 255), Opponent_paddle)
    pygame.draw.ellipse(screen, (255, 255, 255), ball)

    text1 = font.render(str(score1), True, (255, 255, 255))
    text2 = font.render(str(score2), True, (255, 255, 255))

    screen.blit(text1, (screen_width // 4, 50))
    screen.blit(text2, (screen_width // 4, 550))

    move_ball()

    key = pygame.key.get_pressed()

    if key[pygame.K_a] and My_paddle.x >= 5:
        My_paddle.move_ip(-5, 0)
    if key[pygame.K_d] and My_paddle.x <= screen_width - My_paddle.width - 5:
        My_paddle.move_ip(5, 0)

    if key[pygame.K_LEFT] and Opponent_paddle.x >= 5:
        Opponent_paddle.move_ip(-5, 0)
    if key[pygame.K_RIGHT] and Opponent_paddle.x <= screen_width - Opponent_paddle.width - 5:
        Opponent_paddle.move_ip(5, 0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if score1 >= 5 or score2 >= 5:
        winner_text = font.render(f"Wygrał gracz {1 if score1 >= 5 else 2}!", True, (255, 255, 255))
        screen.blit(winner_text, (screen_width // 2 - winner_text.get_width() // 2, screen_height // 2 - winner_text.get_height() // 2))
        pygame.display.flip()
        pygame.time.delay(3000)
        running = False

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
