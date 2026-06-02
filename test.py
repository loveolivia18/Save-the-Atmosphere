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


