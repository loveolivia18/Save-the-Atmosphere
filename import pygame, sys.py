import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mijn Eerste Pygame")

clock = pygame.time.Clock()

dt = 0

player_pos = pygame.Vector2(
    screen.get_width() / 2,
    screen.get_height() / 2
)

running = True
while running:

    # events checken
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # achtergrond
    screen.fill((30, 30, 30))

    # speler tekenen
    pygame.draw.circle(screen, (255, 0, 0), player_pos, 20)

    # scherm updaten
    pygame.display.flip()

    # fps
    clock.tick(60)

pygame.quit()
sys.exit()