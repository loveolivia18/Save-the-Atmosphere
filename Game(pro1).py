import pygame, sys
import math
from pygame.locals import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 1000))
pygame.display.set_caption("*NAAM GAME*")
clock = pygame.time.Clock()

pygame.font.init()
titel_font = pygame.font.SysFont("Arial", 60, bold=True)
knop_font = pygame.font.SysFont("Arial", 30)
uitleg_font = pygame.font.SysFont("Arial", 30)
naam_font = pygame.font.SysFont("Arial", 20, bold=True)
esc_font = pygame.font.SysFont("Arial", 15) 

# Knop en titel posities
titel_y_positie = 300

knop_breedte = 200
knop_hoogte = 60
knop_x = (800 / 2) - (knop_breedte / 2) 
knop_y = 450 
knop_rect = pygame.Rect(knop_x, knop_y, knop_breedte, knop_hoogte) 

huidig_scherm = "startscherm"
info_huidige_planeet = None # Hierin worden gegevens per planeet opgeslagen

dt = 0
vaste_hoogte = 900
player_pos = pygame.Vector2(screen.get_width() / 2, vaste_hoogte)

# Gegevens: (Naam, Kleur, X, Y, Grootte)
ster = ("Zon", "orange", 400, 500, 100)

planeet1 = ("Mercurius", "red", 550, 300, 30)
planeet2 = ("Venus", "green", 200, 600, 40)
planeet3 = ("Mars","brown", 370, 200, 30)
planeet4 = ("Jupiter", "white", 650, 700, 50)
planeet5 = ("Saturnus", "black", 700, 100, 40)
planeet6 = ("Uranus", "grey", 60, 900, 40)
planeet7 = ("Neptunus", "yellow", 60, 50, 40)
planeet8 = ("Aarde", "blue", 300, 750, 40)

planeten = [planeet1, planeet2, planeet3, planeet4, planeet5, planeet6, planeet7, planeet8]

running = True
while running:
    # 1. INPUT (Event Handling)
    for event in pygame.event.get():
        
        # Geforceerde afsluiting als je op het kruisje drukt
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if huidig_scherm == "startscherm":
            # Check voor Spatiebalk
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    huidig_scherm = "uitleg_scherm"
            
            # Check voor Muisklik
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    if knop_rect.collidepoint(event.pos):
                        huidig_scherm = "uitleg_scherm"
        
        elif huidig_scherm == "uitleg_scherm":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: #K_RETURN is de 'Enter' toets
                    huidig_scherm = "game"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # 1 = linker muisknop
                    
                    for planeet in planeten:
                        naam, kleur, x, y, grootte = planeet

                        if math.dist(event.pos, (x, y)) <= grootte: # Checken of de muis zich in de cirkel bevindt
                            print("Je hebt geklikt op:", naam)
                            huidig_scherm = naam 
                            info_huidige_planeet = planeet # Hier worden de planeet gegevens onthouden
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Druk op ESC om terug te gaan
                    huidig_scherm = "uitleg_scherm"

    # Delta time berekenen
    dt = clock.tick(60) / 1000

    # 2. SCHERM TEKENEN & LOGICA
    if huidig_scherm == "startscherm":
        screen.fill("green") 
        
        # Titel
        titel_tekst = titel_font.render("*GAME NAME*", True, "black")
        titel_x = (800 / 2) - (titel_tekst.get_width() / 2)
        screen.blit(titel_tekst, (titel_x, titel_y_positie))
        
        # Knop
        pygame.draw.rect(screen, "black", knop_rect)
        
        # Tekst op knop
        knop_tekst = knop_font.render("START", True, "white")
        knop_tekst_x = knop_x + (knop_breedte / 2) - (knop_tekst.get_width() / 2)
        knop_tekst_y = knop_y + (knop_hoogte / 2) - (knop_tekst.get_height() / 2)
        screen.blit(knop_tekst, (knop_tekst_x, knop_tekst_y)) 

    elif huidig_scherm == "game":
        screen.fill("green")
        pygame.draw.circle(screen, "black", player_pos, 25)

        # Besturing van de bal
        ruimteschip = pygame.key.get_pressed()
        if ruimteschip[pygame.K_d]:
            player_pos.x += 400 * dt
        if ruimteschip[pygame.K_a]:
            player_pos.x -= 400 * dt

    elif huidig_scherm == "uitleg_scherm":
        screen.fill("purple")

        # 1. De ster (Zon) correct tekenen met de juiste index-nummers
        pygame.draw.circle(screen, ster[1], (ster[2], ster[3]), ster[4])
        ster_tekst = naam_font.render(ster[0], True, "white")
        ster_tekst_x = ster[2] - (ster_tekst.get_width() / 2)
        screen.blit(ster_tekst, (ster_tekst_x, ster[3] - ster[4] - 25))

        # 2. Loop die zowel de cirkel van de planeten als hun namen op het scherm zet
        for naam, kleur, x, y, grootte in planeten: 
            pygame.draw.circle(screen, kleur, (x, y), grootte)
            
            p_tekst = naam_font.render(naam, True, "white") 
            p_tekst_x = x - (p_tekst.get_width() / 2) 
            screen.blit(p_tekst, (p_tekst_x, y - grootte - 25))
    elif huidig_scherm in ["Mercurius", "Venus", "Mars", "Jupiter", "Saturnus", "Uranus", "Neptunus", "Aarde"]:
        if info_huidige_planeet:
            naam, kleur, x, y, grootte = info_huidige_planeet

            screen.fill(kleur) # vul het scherm met de kleur van de gekozen planeet
            tekst_kleur = "white" if kleur == "black" else "black" # Als de kleur van de planeet zwart is, voeg dan wit als tekst
            titel = titel_font.render(naam, True, tekst_kleur) # Teken de naam van de planeet
            screen.blit(titel, ((800/2) - (titel.get_width() /2), 200))
            terug_tekst = esc_font.render("Druk op ESC om terug naar het planeten menu te gaan.", True, tekst_kleur)
            screen.blit(terug_tekst, (10, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()