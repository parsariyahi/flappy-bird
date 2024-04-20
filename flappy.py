from pathlib import Path
import pygame

pygame.init()

CURRENT_WORKING_DIR = Path().resolve()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Flappy bird", str(CURRENT_WORKING_DIR / Path("assets/img/bird.png")))

clock = pygame.time.Clock()
FPS = 60

bg_img = pygame.image.load(CURRENT_WORKING_DIR / Path("assets/img/bg-resized.png"))
bg_rect = bg_img.get_rect()
bg_rect.topleft = (0, 0)


"""
pip green png:
    height = 160
"""
pipe_green_down = pygame.image.load(CURRENT_WORKING_DIR / Path("assets/img/pipe-green.png"))
pipe_green_down_rect = pipe_green_down.get_rect()
pipe_green_down_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 30)

pipe_green_up_img = pygame.transform.flip(pipe_green_down, True, True)
pipe_green_up_rect = pipe_green_up_img.get_rect()
pipe_green_up_rect.center = (WINDOW_WIDTH // 2, 100)

pipe_red_img = pygame.image.load(CURRENT_WORKING_DIR / Path("assets/img/pipe-red.png"))
pipe_red_rect = pipe_red_img.get_rect()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill((0, 0, 0))
    display_surface.blit(bg_img, bg_rect)
    display_surface.blit(pipe_green_down, pipe_green_down_rect)
    display_surface.blit(pipe_green_up_img, pipe_green_up_rect)

    pygame.display.update()
    clock.tick(FPS)


pygame.quit()