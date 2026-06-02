import pygame, sys
from pygame.locals import *

pygame.init()
scherm = pygame.display.set_mode((800, 600))

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mijn Eerste Pygame")
clock = pygame.time.Clock()

dt = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

running = True
while running:
    screen.fill("blue")
    dt = clock.tick(60) / 1000 
    pygame.draw.circle(screen, "red", player_pos, 30)

    ruimteschip = pygame.key.get_pressed()
    if ruimteschip[pygame.K_w]:
        player_pos.y -= 300 * dt
    if ruimteschip[pygame.K_s]:
        player_pos.y += 300 * dt
    if ruimteschip[pygame.K_d]:
        player_pos.x += 300 * dt
    if ruimteschip[pygame.K_a]:
        player_pos.x -= 300 * dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()

pygame.quit()



