import pygame, sys, random

WIDTH, HEIGHT = 800, 600
BLOCK_SIZE = 20
SPEED = 10

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

font = pygame.font.Font(None, 36)

snake = [(200, 200), (220, 200), (240, 200)]
food = (random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE,
                random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE)

direction = 'RIGHT'

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif e.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            elif e.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif e.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'
    
    head = snake[-1]
    if direction == 'UP':
        new_head = (head[0], head[1] - BLOCK_SIZE)
    elif direction == 'DOWN':
        new_head = (head[0], head[1] + BLOCK_SIZE)
    elif direction == 'LEFT':
        new_head = (head[0] - BLOCK_SIZE, head[1])
    elif direction == 'RIGHT':
        new_head = (head[0] + BLOCK_SIZE, head[1])
    
    snake.append(new_head)

    if (snake[-1][0] < 0 or snake[-1][0] >= WIDTH or
    snake[-1][1] < 0 or snake[-1][1] >= HEIGHT or
    snake[-1] in snake[:-1]):
        print("Game Over")
        pygame.quit()
        sys.exit()
    
    if snake[-1] == food:
        food = (random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE,
                random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE)
    else:
        snake.pop(0)
    
    screen.fill(BLACK)
    for pos in snake:
        pygame.draw.rect(screen, GREEN, (pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, RED, (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))
    text = font.render(f"Score: {len(snake)}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.flip()
    pygame.time.Clock().tick(SPEED)