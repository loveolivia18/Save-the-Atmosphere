import pygame
import sys

pygame.init()
breedte, hoogte = 600, 400
scherm = pygame.display.set_mode((breedte, hoogte))
pygame.display.set_caption("Windows Stuiter Cirkel")
klok = pygame.time.Clock()

x, y = 100, 100
stap_x, stap_y = 5, 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    x += stap_x
    y += stap_y

    # Botsing detectie
    if x > breedte - 20 or x < 20: stap_x *= -1
    if y > hoogte - 20 or y < 20: stap_y *= -1

    scherm.fill((20, 20, 20)) # Donkergrijs
    pygame.draw.circle(scherm, (0, 200, 255), (x, y), 20) # Blauwe cirkel
    pygame.display.flip()
    klok.tick(60)
