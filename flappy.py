from pathlib import Path
import random
import pygame

pygame.init()

CURRENT_WORKING_DIR = Path().resolve()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Flappy bird", str(CURRENT_WORKING_DIR / Path("assets/img/bird.png")))

BIRD_GRAVITY = 1
BIRD_JUMP_SIZE = 40
PIPE_STARTING_VELOCITY = 0.5
PIPE_ACCELERATION = 0.01
PIPE_BUFFER_SIZE = 400

clock = pygame.time.Clock()
FPS = 60

pipe_velocity = PIPE_STARTING_VELOCITY

bg_img = pygame.image.load(CURRENT_WORKING_DIR / Path("assets/img/bg-resized.png"))
bg_rect = bg_img.get_rect()
bg_rect.topleft = (0, 0)

bird_img = pygame.image.load(CURRENT_WORKING_DIR / Path("assets/img/bird.png"))
bird_rect = bird_img.get_rect()
bird_rect.center = (WINDOW_WIDTH // 2 - 200, WINDOW_HEIGHT // 2)


"""
pip green png:
    height = 160
"""
pipe_green_down = pygame.image.load(CURRENT_WORKING_DIR / Path("assets/img/pipe-green.png"))
pipe_green_down_rect = pipe_green_down.get_rect()
pipe_green_down_rect.center = (WINDOW_WIDTH + PIPE_BUFFER_SIZE , WINDOW_HEIGHT - random.randint(40, 100))

pipe_green_up_img = pygame.transform.flip(pipe_green_down, True, True)
pipe_green_up_rect = pipe_green_up_img.get_rect()
pipe_green_up_rect.center = (WINDOW_WIDTH + PIPE_BUFFER_SIZE , random.randint(40, 100))

pipe_red_img = pygame.image.load(CURRENT_WORKING_DIR / Path("assets/img/pipe-red.png"))
pipe_red_rect = pipe_red_img.get_rect()

running = True
while running:
    gravity_effect = True
    jump = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_rect.y -= BIRD_JUMP_SIZE
                gravity_effect = False


    pipe_green_down_rect.x -= pipe_velocity
    pipe_green_up_rect.x -= pipe_velocity
    pipe_velocity += PIPE_ACCELERATION

    if pipe_green_up_rect.x <= 0:
        pipe_green_down_rect.center = (WINDOW_WIDTH + PIPE_BUFFER_SIZE , WINDOW_HEIGHT - random.randint(40, 160))
        pipe_green_up_rect.center = (WINDOW_WIDTH + PIPE_BUFFER_SIZE , random.randint(40, 160))

    display_surface.fill((0, 0, 0))
    display_surface.blit(bg_img, bg_rect)
    display_surface.blit(bird_img, bird_rect)
    display_surface.blit(pipe_green_down, pipe_green_down_rect)
    display_surface.blit(pipe_green_up_img, pipe_green_up_rect)

    pygame.display.update()
    clock.tick(FPS)

    if gravity_effect:
        bird_rect.centery += BIRD_GRAVITY

pygame.quit()