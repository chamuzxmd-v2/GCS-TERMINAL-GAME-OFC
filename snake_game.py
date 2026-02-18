import pygame, sys, random
from pygame.locals import *

def play_snake():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('🐍 Snake Game')

    WHITE = (255,255,255)
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLACK = (0,0,0)

    snake_pos = [[250,250]]
    snake_body = 10
    direction = 'RIGHT'
    change_to = direction
    food_pos = [random.randrange(1,50)*10, random.randrange(1,50)*10]
    score = 0

    font = pygame.font.SysFont('Arial', 20)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    change_to = 'UP'
                elif event.key == K_DOWN:
                    change_to = 'DOWN'
                elif event.key == K_LEFT:
                    change_to = 'LEFT'
                elif event.key == K_RIGHT:
                    change_to = 'RIGHT'

        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        if direction == 'UP':
            snake_pos[0][1] -= 10
        if direction == 'DOWN':
            snake_pos[0][1] += 10
        if direction == 'LEFT':
            snake_pos[0][0] -= 10
        if direction == 'RIGHT':
            snake_pos[0][0] += 10

        snake_pos.insert(0, list(snake_pos[0]))
        if snake_pos[0] == food_pos:
            score += 1
            food_pos = [random.randrange(1,50)*10, random.randrange(1,50)*10]
        else:
            snake_pos.pop()

        screen.fill(BLACK)
        for pos in snake_pos:
            pygame.draw.rect(screen, GREEN, Rect(pos[0], pos[1], snake_body, snake_body))
        pygame.draw.rect(screen, RED, Rect(food_pos[0], food_pos[1], snake_body, snake_body))

        for block in snake_pos[1:]:
            if snake_pos[0] == block:
                pygame.quit()
                return

        if snake_pos[0][0]<0 or snake_pos[0][0]>=500 or snake_pos[0][1]<0 or snake_pos[0][1]>=500:
            pygame.quit()
            return

        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, [10,10])
        pygame.display.update()
        clock.tick(15)
