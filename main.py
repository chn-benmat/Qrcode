import pygame
import random

pygame.init()

# กำหนดขนาดหน้าจอ
WIDTH, HEIGHT = 640, 480
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# กำหนดสี
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)

# กำหนดขนาดเซลล์
CELL_SIZE = 10

# สร้างงู
snake = [(3, 3)]
snake_direction = (1, 0)

# สร้างอาหาร
food = (random.randint(0, WIDTH // CELL_SIZE - 1), random.randint(0, HEIGHT // CELL_SIZE - 1))

# กำหนดคะแนน
score = 0

# สร้างฟอนต์
font = pygame.font.Font(None, 26)

# สร้างเวลา
clock = pygame.time.Clock()

# กำหนดความเร็วเริ่มต้น
speed = 10

# กำหนดเกมส์เริ่มต้น
game_over = False
game_stop = False
start_time = pygame.time.get_ticks() // 1000
previous_stop_time = 0
elapsed_time = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        pygame.quit()
        exit()
    elif keys[pygame.K_r]:
        snake = [(3, 3)]
        snake_direction = (1, 0)
        food = (random.randint(0, WIDTH // CELL_SIZE - 1), random.randint(0, HEIGHT // CELL_SIZE - 1))
        score = 0
        speed = 10
        start_time = pygame.time.get_ticks() // 1000
        game_over = False
        game_stop = False

    if not game_over and not game_stop:
        if keys[pygame.K_UP]:
            snake_direction = (0, -1)
        elif keys[pygame.K_DOWN]:
            snake_direction = (0, 1)
        elif keys[pygame.K_LEFT]:
            snake_direction = (-1, 0)
        elif keys[pygame.K_RIGHT]:
            snake_direction = (1, 0)

        head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
        snake.insert(0, head)

        if head == food:
            food = (random.randint(0, WIDTH // CELL_SIZE - 1), random.randint(0, HEIGHT // CELL_SIZE - 1))
            score += 10
            speed += 1
        else:
            snake.pop()

        if head in snake[1:] or head[0] < 0 or head[0] >= WIDTH // CELL_SIZE or head[1] < 0 or head[1] >= HEIGHT // CELL_SIZE:
            game_over = True
            game_stop = True

    win.fill(BLACK)
    pygame.draw.rect(win, ORANGE, (food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    for segment in snake:
        pygame.draw.rect(win, WHITE, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    if game_over:
        if not game_stop:
            stop_time = pygame.time.get_ticks() // 1000 - start_time
            elapsed_time += stop_time - previous_stop_time
            previous_stop_time = stop_time
        else:
            previous_stop_time = pygame.time.get_ticks() // 1000 - start_time

        game_over_text = font.render("Game Over", True, WHITE)
        win.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))
        score_text = font.render(f"Score: {score}", True, WHITE)
        win.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 + 10))
        time_text = font.render(f"Total Time: {elapsed_time} seconds", True, WHITE)
        win.blit(time_text, (WIDTH // 2 - time_text.get_width() // 2, HEIGHT // 2 + 30))
        restart_text = font.render("Press R to Restart or Q to Quit", True, WHITE)
        win.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 50))
    else:
        text = font.render(f"Score: {score}", True, WHITE)
        win.blit(text, (10, 10))

        speed_text = font.render(f"Speed: {speed}", True, WHITE)
        win.blit(speed_text, (10, 36))

        elapsed_time = pygame.time.get_ticks() // 1000 - start_time
        time_text = font.render(f"Time: {elapsed_time}", True, WHITE)
        win.blit(time_text, (WIDTH - time_text.get_width() - 10, 10))

    pygame.display.update()

    clock.tick(speed)

pygame.quit()
