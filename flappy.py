from pathlib import Path
import pygame

pygame.init()

CURRENT_WORKING_DIR = Path().resolve()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

clock = pygame.time.Clock()
FPS = 60

bg_img = pygame.image.load(CURRENT_WORKING_DIR / Path("assets/img/bg-resized.png"))
bg_rect = bg_img.get_rect()
bg_rect.topleft = (0, 0)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill((0, 0, 0))
    display_surface.blit(bg_img, bg_rect)

    pygame.display.update()
    clock.tick(FPS)


pygame.quit()