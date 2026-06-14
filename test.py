#Verticale Display & Basis Besturing:
import pygame
import sys

pygame.init()

SCHERM_BREEDTE = 400
SCHERM_HOOGTE = 700
scherm = pygame.display.set_mode((SCHERM_BREEDTE, SCHERM_HOOGTE))
pygame.display.set_caption("Save the Atmosphere - Prototype 1")

ZWART = (0, 0, 0)
WIT = (255, 255, 255)

lettertype = pygame.font.SysFont("Arial", 24)

running = True
while running:
    # Check of de speler het spel afsluit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Maak het scherm zwart
    scherm.fill(ZWART)

    # Teken een simpele test-tekst in het midden
    tekst = lettertype.render("Start van de game!", True, WIT)
    scherm.blit(tekst, (100, 320))

    # Update het scherm zodat je de veranderingen ziet
    pygame.display.flip()

pygame.quit()
sys.exit()


#---------------------------------------------------------------------------------------------------------------


#Ruimteschip (Illustratie 1):
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ruimteschip Bovenaanzicht")
clock = pygame.time.Clock()

# Kleuren
BG_COLOR = (10, 15, 30)
SHIP_COLOR = (200, 200, 220)
WING_COLOR = (100, 110, 130)
THRUST_COLOR = (255, 100, 0)
COCKPIT_COLOR = (0, 180, 255)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BG_COLOR)
    cx, cy = 400, 300

    # Ruimteschip tekenen
    pygame.draw.polygon(screen, THRUST_COLOR, [(cx - 10, cy + 40), (cx, cy + 65), (cx + 10, cy + 40)])
    pygame.draw.polygon(screen, WING_COLOR, [(cx - 20, cy + 10), (cx - 50, cy + 35), (cx - 20, cy + 35)])
    pygame.draw.polygon(screen, WING_COLOR, [(cx + 20, cy + 10), (cx + 50, cy + 35), (cx + 20, cy + 35)])
    pygame.draw.polygon(screen, SHIP_COLOR, [(cx, cy - 50), (cx - 25, cy + 40), (cx + 25, cy + 40)])
    pygame.draw.polygon(screen, COCKPIT_COLOR, [(cx, cy - 35), (cx - 10, cy - 5), (cx + 10, cy - 5)])

    pygame.display.flip()
    clock.tick(60)


    #---------------------------------------------------------------------------------------------------------------

    
    #Schietmechanic & Kogels (Illustratie 2):
    import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Schietmechanic & UI")
clock = pygame.time.Clock()

BG_COLOR = (10, 15, 30)
LASER_COLOR = (100, 255, 100)
UI_COLOR = (50, 200, 50)
font = pygame.font.Font(None, 24)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BG_COLOR)
    cx, cy = WIDTH // 2, HEIGHT // 2

    # Laserstraal
    laser_rect = pygame.Rect(cx - 4, cy - 200, 8, 140)
    pygame.draw.rect(screen, LASER_COLOR, laser_rect)
    pygame.draw.rect(screen, (200, 255, 200), (cx - 2, cy - 200, 4, 140))

    # UI Elementen (Rechtsboven)
    ui_box = pygame.Rect(WIDTH - 70, 30, 40, 40)
    pygame.draw.rect(screen, UI_COLOR, ui_box, 2)
    q_text = font.render("Q", True, UI_COLOR)
    screen.blit(q_text, (WIDTH - 57, 40))
    
    ammo_text = font.render("AMMO: 50", True, UI_COLOR)
    screen.blit(ammo_text, (WIDTH - 110, 80))

    pygame.display.flip()
    clock.tick(60)


#---------------------------------------------------------------------------------------------------------------


#Basis Vijand (Illustratie 3):
import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basis Vijand")
clock = pygame.time.Clock()

BG_COLOR = (10, 15, 30)
ENEMY_BODY = (120, 40, 140)
ENEMY_GLOW = (0, 255, 150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BG_COLOR)
    ex, ey = WIDTH // 2, 120

    # De Basis Vijand (UFO)
    pygame.draw.line(screen, ENEMY_GLOW, (ex - 60, ey), (ex - 80, ey - 10), 4)
    pygame.draw.line(screen, ENEMY_GLOW, (ex + 60, ey), (ex + 80, ey - 10), 4)
    pygame.draw.circle(screen, ENEMY_GLOW, (ex - 80, ey - 10), 5)
    pygame.draw.circle(screen, ENEMY_GLOW, (ex + 80, ey - 10), 5)
    pygame.draw.ellipse(screen, ENEMY_BODY, (ex - 60, ey - 25, 120, 50))
    pygame.draw.arc(screen, ENEMY_GLOW, (ex - 30, ey - 35, 60, 40), 0, 3.14, 4)
    pygame.draw.ellipse(screen, (30, 80, 70), (ex - 25, ey - 25, 50, 20))
    pygame.draw.circle(screen, ENEMY_GLOW, (ex - 35, ey + 5), 6)
    pygame.draw.circle(screen, ENEMY_GLOW, (ex, ey + 10), 6)
    pygame.draw.circle(screen, ENEMY_GLOW, (ex + 35, ey + 5), 6)

    pygame.display.flip()
    clock.tick(60)

 #---------------------------------------------------------------------------------------------------------------

 #UI-Elementen (Hartjes/Levens):
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Levens UI")
clock = pygame.time.Clock()

BG_COLOR = (10, 15, 30)
UI_COLOR = (50, 200, 50)
HEART_COLOR = (255, 50, 50)
font = pygame.font.Font(None, 24)

def draw_heart(surface, color, x, y, size):
    radius = size // 4
    pygame.draw.circle(surface, color, (x - radius, y), radius)
    pygame.draw.circle(surface, color, (x + radius, y), radius)
    pygame.draw.polygon(surface, color, [
        (x - radius * 2, y + radius // 2), 
        (x + radius * 2, y + radius // 2), 
        (x, y + size // 2 + radius)
    ])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BG_COLOR)

    # UI Hartjes / Levens (Linksboven)
    lives = 3
    start_x = 40
    spacing = 45
    
    for i in range(lives):
        box_rect = pygame.Rect(start_x + (i * spacing) - 20, 25, 40, 45)
        pygame.draw.rect(screen, UI_COLOR, box_rect, 2)
        draw_heart(screen, HEART_COLOR, start_x + (i * spacing), 40, 24)
    
    lives_text = font.render(f"LIVES: {lives}", True, UI_COLOR)
    screen.blit(lives_text, (20, 80))

    pygame.display.flip()
    clock.tick(60)

#---------------------------------------------------------------------------------------------------------------

#Het Boost-Systeem (Visueel):
import pygame
import sys

# Initialisatie
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Geïsoleerd Boost-Systeem")
clock = pygame.time.Clock()

# Basis kleuren
BG_COLOR = (10, 15, 30)
SHIP_COLOR = (200, 200, 220)
WING_COLOR = (100, 110, 130)
COCKPIT_COLOR = (0, 180, 255)
TEXT_COLOR = (255, 255, 255)

# Specifieke Boost & Vlam kleuren
NORMAL_FLAME = (255, 100, 0)     # Standaard oranje
BOOST_OUTER = (0, 150, 255)      # Intense blauwe buitenkant
BOOST_INNER = (255, 255, 255)    # Hete witte kern

font = pygame.font.Font(None, 24)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Kijken of de spatiebalk ingedrukt wordt gehouden
    keys = pygame.key.get_pressed()
    boost_actief = keys[pygame.K_SPACE]

    # Scherm opschonen
    screen.fill(BG_COLOR)
    
    # Ruimteschip positie (midden van het scherm)
    cx, cy = WIDTH // 2, HEIGHT // 2

    # --- BOOST VISUELE EFFECTEN ---
    if boost_actief:
        # 1. Energie-gloed achter het schip (transparante cirkel via een extra Surface)
        glow_surface = pygame.Surface((120, 120), pygame.SRCALPHA)
        pygame.draw.circle(glow_surface, (0, 100, 255, 40), (60, 60), 50)
        screen.blit(glow_surface, (cx - 60, cy + 10))

        # 2. Grote blauwe boost-vlam
        pygame.draw.polygon(screen, BOOST_OUTER, [(cx - 15, cy + 40), (cx, cy + 95), (cx + 15, cy + 40)])
        
        # 3. Witte kernvlam voor extra hitte-effect
        pygame.draw.polygon(screen, BOOST_INNER, [(cx - 7, cy + 40), (cx, cy + 65), (cx + 7, cy + 40)])
        
        # Status tekst op het scherm
        status_text = font.render("BOOST ACTIEF: Snelheid + | Wapens: GEBLOKKEERD", True, (255, 80, 80))
    else:
        # Standaard kleine oranje motorvlam
        pygame.draw.polygon(screen, NORMAL_FLAME, [(cx - 10, cy + 40), (cx, cy + 65), (cx + 10, cy + 40)])
        
        # Status tekst op het scherm
        status_text = font.render("Wapens: Standby | Houd SPATIEBALK ingedrukt voor Boost", True, (100, 200, 100))

    # --- HET RUIMTESCHIP ---
    pygame.draw.polygon(screen, WING_COLOR, [(cx - 20, cy + 10), (cx - 50, cy + 35), (cx - 20, cy + 35)])
    pygame.draw.polygon(screen, WING_COLOR, [(cx + 20, cy + 10), (cx + 50, cy + 35), (cx + 20, cy + 35)])
    pygame.draw.polygon(screen, SHIP_COLOR, [(cx, cy - 50), (cx - 25, cy + 40), (cx + 25, cy + 40)])
    pygame.draw.polygon(screen, COCKPIT_COLOR, [(cx, cy - 35), (cx - 10, cy - 5), (cx + 10, cy - 5)])

    # Tekst op het scherm zetten
    screen.blit(status_text, (20, 20))

    pygame.display.flip()
    clock.tick(60)

    #---------------------------------------------------------------------------------------------------------------

    #De Hub (Planeten Selectiescherm):
    import pygame
import sys

# Initialisatie
pygame.init()
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("De Hub - Planeten Selectiescherm")
clock = pygame.time.Clock()

# Kleuren
BG_COLOR = (5, 10, 25)       # Diep donkerblauw (ruimte)
TEXT_COLOR = (200, 220, 255)
HOVER_COLOR = (255, 255, 255)

# Planetendata: (Naam, Kleur, Straal/Grootte, X-positie, Y-positie)
PLANETS = [
    {"name": "Mercurius", "color": (165, 165, 165), "radius": 12, "x": 100, "y": 300},
    {"name": "Venus",     "color": (225, 190, 130), "radius": 20, "x": 200, "y": 300},
    {"name": "Aarde",     "color": (50, 130, 225),  "radius": 22, "x": 320, "y": 300},
    {"name": "Mars",      "color": (210, 80, 50),   "radius": 16, "x": 440, "y": 300},
    {"name": "Jupiter",   "color": (215, 165, 120), "radius": 45, "x": 580, "y": 300},
    {"name": "Saturnus",  "color": (230, 210, 160), "radius": 38, "x": 730, "y": 300},
    {"name": "Uranus",    "color": (160, 220, 225), "radius": 28, "x": 860, "y": 300},
    {"name": "Neptunus",  "color": (60, 90, 190),   "radius": 26, "x": 940, "y": 300}
]

font = pygame.font.Font(None, 24)
title_font = pygame.font.Font(None, 36)

while True:
    # Muispositie ophalen
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Scherm leegmaken
    screen.fill(BG_COLOR)

    # Titels tekenen
    title_text = title_font.render("SELECTEER EEN PLANEET", True, TEXT_COLOR)
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 50))
    
    instruction_text = font.render("Beweeg je muis over een planeet om deze te bekijken", True, (100, 130, 170))
    screen.blit(instruction_text, (WIDTH // 2 - instruction_text.get_width() // 2, 90))

    # Alle 8 planeten tekenen
    for planet in PLANETS:
        px, py = planet["x"], planet["y"]
        radius = planet["radius"]
        
        # Bereken of de muis bovenop de planeet staat (met de stelling van Pythagoras)
        distance = ((mouse_x - px) ** 2 + (mouse_y - py) ** 2) ** 0.5
        is_hovered = distance <= radius

        # Speciale details per planeet (zoals de ringen van Saturnus)
        if planet["name"] == "Saturnus":
            # Teken de ringen achter/onder de planeet
            ring_color = (180, 160, 120)
            pygame.draw.ellipse(screen, ring_color, (px - 60, py - 10, 120, 20), 3)

        # De planeet zelf tekenen
        pygame.draw.circle(screen, planet["color"], (px, py), radius)

        # Visuele feedback bij mouse-hover
        if is_hovered:
            # Teken een selectiering om de planeet heen
            pygame.draw.circle(screen, HOVER_COLOR, (px, py), radius + 6, 2)
            
            # Toon de naam van de planeet boven de planeet
            name_text = font.render(planet["name"], True, HOVER_COLOR)
            screen.blit(name_text, (px - name_text.get_width() // 2, py - radius - 30))
        else:
            # Toon de naam subtiel onder de planeet als er geen hover is
            name_text = font.render(planet["name"], True, (100, 120, 150))
            screen.blit(name_text, (px - name_text.get_width() // 2, py + 60))

    pygame.display.flip()
    clock.tick(60)

#---------------------------------------------------------------------------------------------------------------

#Een duidelijke Slot-illustratie over de aarde heen.
import pygame
import sys

# Initialisatie
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aarde met Slot-Illustratie")
clock = pygame.time.Clock()

# Kleuren
BG_COLOR = (10, 15, 30)
EARTH_BLUE = (50, 130, 225)
EARTH_GREEN = (60, 180, 100)
LOCK_BODY = (220, 160, 40)     # Goud/messing kleur voor het slot
LOCK_SHACKLE = (140, 140, 150) # Grijs voor de beugel
KEYHOLE = (20, 20, 25)         # Donkergrijs voor het sleutelgat

font = pygame.font.Font(None, 28)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BG_COLOR)

    # Middelpunt voor de Aarde en het slot
    cx, cy = WIDTH // 2, HEIGHT // 2
    earth_radius = 120

    # --- 1. DE AARDE TEKENEN ---
    # Basis oceaan (Blauwe cirkel)
    pygame.draw.circle(screen, EARTH_BLUE, (cx, cy), earth_radius)
    
    # Simpele continenten/landmassa's binnen de cirkel (Groene polygonen/ellipsen)
    pygame.draw.ellipse(screen, EARTH_GREEN, (cx - 80, cy - 70, 70, 50))
    pygame.draw.ellipse(screen, EARTH_GREEN, (cx + 10, cy - 40, 90, 60))
    pygame.draw.polygon(screen, EARTH_GREEN, [(cx - 60, cy + 10), (cx - 10, cy + 80), (cx - 90, cy + 40)])
    pygame.draw.polygon(screen, EARTH_GREEN, [(cx + 20, cy + 30), (cx + 70, cy + 70), (cx + 80, cy + 20)])

    # --- 2. HET SLOT ERBOVENOP TEKENEN ---
    # A. De metalen beugel (Grijze boog/lijn boven het slot)
    # We tekenen een dikke cirkelrand en snijden de onderkant visueel af met de romp van het slot
    shackle_rect = pygame.Rect(cx - 35, cy - 70, 70, 70)
    pygame.draw.ellipse(screen, LOCK_SHACKLE, shackle_rect, 10)

    # B. De romp van het slot (Gouden rechthoek met afgeronde hoeken)
    lock_rect = pygame.Rect(cx - 45, cy - 15, 90, 75)
    pygame.draw.rect(screen, LOCK_BODY, lock_rect, border_radius=8)
    
    # Extra detail: een glanzende rand op het slot
    pygame.draw.rect(screen, (245, 200, 80), lock_rect, 3, border_radius=8)

    # C. Het sleutelgat (Cirkel + Driehoek onderkant)
    pygame.draw.circle(screen, KEYHOLE, (cx, cy + 10), 10)
    pygame.draw.polygon(screen, KEYHOLE, [(cx - 6, cy + 14), (cx + 6, cy + 14), (cx + 10, cy + 35), (cx - 10, cy + 35)])

    # --- 3. TEKST INDICATOR ---
    text = font.render("EINDLEVEL VERGRENDELD", True, (255, 100, 100))
    screen.blit(text, (cx - text.get_width() // 2, cy + 100))

    pygame.display.flip()
    clock.tick(60)
 
#---------------------------------------------------------------------------------------------------------------

#Achtergrond-illustratie:
import pygame
import sys
import random

# Initialisatie
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Geïsoleerd Effect: Zon aanval op Aarde")
clock = pygame.time.Clock()

# Kleuren
BG_COLOR = (5, 10, 20)       # Diepe ruimte
SUN_COLOR = (255, 150, 0)    # Oranje/Geel
SUN_CORE = (255, 255, 200)   # Witte kern
RAY_COLOR = (255, 50, 0)     # Rode aanvalsstralen
EARTH_BLUE = (50, 130, 225)
EARTH_GREEN = (60, 180, 100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BG_COLOR)

    # Middelpunten
    sun_cx, sun_cy = 0, HEIGHT // 2      # Zon aan de linkerkant
    earth_cx, earth_cy = WIDTH - 150, HEIGHT // 2 # Aarde aan de rechterkant

    # --- 1. DE AANVALSSTRALEN TEKENEN ---
    num_rays = 12
    for i in range(num_rays):
        # Willekeurige lengte en variatie voor de stralen om de aanval te simuleren
        ray_len = random.randint(WIDTH // 2, WIDTH - 200)
        angle_var = random.uniform(-20, 20) # Kleine hoekvariatie
        
        # Eindpunt van de straal
        end_x = sun_cx + ray_len
        end_y = sun_cy + angle_var
        
        # Teken de dikke aanvalsstraal richting de Aarde
        pygame.draw.line(screen, RAY_COLOR, (sun_cx, sun_cy), (end_x, end_y), 8)
        # Dunner felgeel detail
        pygame.draw.line(screen, (255, 255, 0), (sun_cx, sun_cy), (end_x, end_y), 2)

    # --- 2. DE ZON TEKENEN ---
    pygame.draw.circle(screen, SUN_COLOR, (sun_cx, sun_cy), 150)
    pygame.draw.circle(screen, SUN_CORE, (sun_cx, sun_cy), 100) # Hete kern

    # --- 3. DE AARDE TEKENEN ---
    pygame.draw.circle(screen, EARTH_BLUE, (earth_cx, earth_cy), 100)
    # Simpele continenten
    pygame.draw.ellipse(screen, EARTH_GREEN, (earth_cx - 60, earth_cy - 50, 60, 40))
    pygame.draw.ellipse(screen, EARTH_GREEN, (earth_cx + 10, earth_cy - 20, 70, 50))
    pygame.draw.polygon(screen, EARTH_GREEN, [(earth_cx - 40, earth_cy + 20), (earth_cx, earth_cy + 70), (earth_cx - 70, earth_cy + 50)])

    pygame.display.flip()
    clock.tick(15) # Lage framerate voor de flitsende stralen

#---------------------------------------------------------------------------------------------------------------

#Thematische Vijanden & Obstakels (Per Planeet):

#Mercurius: Het scherm krijgt een felle wit/gele flits-illustratie (hittegolf).
import pygame
import sys
import random

# Initialisatie
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Geïsoleerd Effect: Mercurius Hittegolf")
clock = pygame.time.Clock()

# Kleuren
BG_COLOR = (10, 15, 30)
WHITE_FLASH = (255, 255, 255)
YELLOW_FLASH = (255, 255, 100)
TEXT_COLOR = (255, 255, 255)

font = pygame.font.Font(None, 36)

# Status variabele om de flits-interval te timen
last_flash_time = pygame.time.get_ticks()
current_bg = BG_COLOR

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # --- 1. HITTEGOLF LOGICA & FLITSEN ---
    current_time = pygame.time.get_ticks()
    
    # Elke 150 tot 400 milliseconden een nieuwe flits
    if current_time - last_flash_time > random.randint(150, 400):
        # Willekeurig wit of geel flitsen
        current_bg = random.choice([WHITE_FLASH, YELLOW_FLASH])
        last_flash_time = current_time
    else:
        # Terug naar de normale ruimte-kleur
        current_bg = BG_COLOR

    # Scherm vullen met de huidige (flitsende) kleur
    screen.fill(current_bg)

    # --- 2. TEKST INDICATOR ---
    text = font.render("MERCURIUS - EXTREME HITTEGOLF ACTIEF", True, TEXT_COLOR)
    # Zwarte rand om de tekst leesbaar te houden tijdens de flitsen
    text_bg = font.render("MERCURIUS - EXTREME HITTEGOLF ACTIEF", True, (0, 0, 0))
    screen.blit(text_bg, (WIDTH // 2 - text.get_width() // 2 + 2, HEIGHT // 2 + 2))
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))

    pygame.display.flip()
    clock.tick(60)

#---------------------------------------------------------------------------------------------------------------
#Venus: Transparante groene of paarse gaswolk-illustraties die over het scherm zweven.
import pygame
import sys
import random

# Initialisatie
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Geïsoleerd Effect: Venus Gaswolken")
clock = pygame.time.Clock()

# Kleuren
BG_COLOR = (15, 20, 35) # Iets lichtere ruimte
GAS_GREEN = (100, 255, 100)
GAS_PURPLE = (150, 50, 200)
TEXT_COLOR = (255, 255, 255)

font = pygame.font.Font(None, 36)

# --- 1. KLASSE VOOR GASWOLKEN ---
class GasCloud:
    def __init__(self):
        self.reset()

    def reset(self):
        # Willekeurige grootte
        self.width = random.randint(150, 400)
        self.height = random.randint(100, 250)
        # Startpositie (altijd rechtsboven, buiten beeld)
        self.x = WIDTH + self.width
        self.y = random.randint(-self.height, HEIGHT)
        # Willekeurige snelheid (links en een beetje omlaag)
        self.speed_x = random.uniform(-1.0, -2.5)
        self.speed_y = random.uniform(0.1, 0.5)
        # Willekeurige kleur (Groen of Paars)
        self.color = random.choice([GAS_GREEN, GAS_PURPLE])
        # Transparantie (Alpha)
        self.alpha = random.randint(40, 80)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        # Als de wolk volledig van het scherm is, reset hem
        if self.x < -self.width or self.y > HEIGHT:
            self.reset()

    def draw(self, surface):
        # Maak een tijdelijke surface met alpha-kanaal voor transparantie
        temp_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        # Teken een ovaal/ellipse op de temp surface
        pygame.draw.ellipse(temp_surface, (*self.color, self.alpha), (0, 0, self.width, self.height))
        # Zet de temp surface op het hoofdscherm
        surface.blit(temp_surface, (int(self.x), int(self.y)))

# --- 2. WOLKEN AANMAKEN ---
num_clouds = 6
clouds = [GasCloud() for _ in range(num_clouds)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BG_COLOR)

    # --- 3. WOLKEN UPDATEN EN TEKENEN ---
    for cloud in clouds:
        cloud.update()
        cloud.draw(screen)

    # --- 4. TEKST INDICATOR ---
    text = font.render("VENUS - TOXISCHE GASWOLKEN ACTIEF", True, TEXT_COLOR)
    text_bg = font.render("VENUS - TOXISCHE GASWOLKEN ACTIEF", True, (0, 0, 0))
    screen.blit(text_bg, (WIDTH // 2 - text.get_width() // 2 + 2, HEIGHT // 2 + 2))
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))

    pygame.display.flip()
    clock.tick(60)
#---------------------------------------------------------------------------------------------------------------
#Jupiter: Felblauwe bliksemschicht-illustraties die van boven naar beneden schieten.
import pygame
import sys
import random

# Initialisatie
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Geïsoleerd Effect: Jupiter Bliksem")
clock = pygame.time.Clock()

# Kleuren
BG_COLOR = (10, 10, 20)
LIGHTNING_BLUE = (100, 200, 255)
TEXT_COLOR = (255, 255, 255)

font = pygame.font.Font(None, 36)

# Status variabele om de bliksem-interval te timen
last_strike_time = pygame.time.get_ticks()
# Lijst van segmenten voor de huidige bliksemschicht
current_lightning = []

# --- 1. FUNCTIE OM EEN BLIKSEMSCHICHT TE GENEREREN ---
def generate_lightning():
    segments = []
    current_x = random.randint(200, WIDTH - 200)
    current_y = 0
    
    while current_y < HEIGHT:
        # Volgende punt berekenen
        next_x = current_x + random.randint(-40, 40)
        next_y = current_y + random.randint(30, 80)
        
        segments.append(((current_x, current_y), (next_x, next_y)))
        
        current_x = next_x
        current_y = next_y
        
    return segments

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BG_COLOR)

    # --- 2. JUPITER BLIKSEM LOGICA & TEKENEN ---
    current_time = pygame.time.get_ticks()
    
    # Elke 400 tot 1200 milliseconden een nieuwe bliksemschicht
    if current_time - last_strike_time > random.randint(400, 1200):
        current_lightning = generate_lightning()
        last_strike_time = current_time
    else:
        # Na een korte flits, bliksem leegmaken
        if current_time - last_strike_time > 100: # Flits-duur van 100ms
            current_lightning = []

    # De bliksemschicht tekenen
    for start_pos, end_pos in current_lightning:
        pygame.draw.line(screen, LIGHTNING_BLUE, start_pos, end_pos, 5)
        # Dunner wit detail voor de kern
        pygame.draw.line(screen, (255, 255, 255), start_pos, end_pos, 2)

    # --- 3. TEKST INDICATOR ---
    text = font.render("JUPITER - FELBLAUWE BLIKSEM ACTIEF", True, TEXT_COLOR)
    text_bg = font.render("JUPITER - FELBLAUWE BLIKSEM ACTIEF", True, (0, 0, 0))
    screen.blit(text_bg, (WIDTH // 2 - text.get_width() // 2 + 2, HEIGHT // 2 + 2))
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))

    pygame.display.flip()
    clock.tick(60)
#---------------------------------------------------------------------------------------------------------------
#Saturnus: Meerdere variaties van ruimtepuin/meteoriet-illustraties.
import pygame
import sys
import random

# Initialisatie
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Geïsoleerd Effect: Saturnus Ruimtepuin")
clock = pygame.time.Clock()

# Kleuren
BG_COLOR = (10, 15, 30)
DEBRIS_COLOR1 = (180, 160, 120)  # Goud/Bruin
DEBRIS_COLOR2 = (140, 140, 150)  # Grijs
TEXT_COLOR = (255, 255, 255)

font = pygame.font.Font(None, 36)

# --- 1. KLASSE VOOR RUIMTEPUIN ---
class Debris:
    def __init__(self):
        self.reset()

    def reset(self):
        # Startpositie (altijd rechts, buiten beeld)
        self.x = WIDTH + 100
        self.y = random.randint(-100, HEIGHT + 100)
        # Willekeurige snelheid (links en een beetje omlaag)
        self.speed_x = random.uniform(-1.0, -3.0)
        self.speed_y = random.uniform(0.1, 0.6)
        # Willekeurige kleur
        self.color = random.choice([DEBRIS_COLOR1, DEBRIS_COLOR2])
        # Willekeurige vorm-type (Cirkel, Ellips, Polygoon)
        self.shape_type = random.choice(['circle', 'ellipse', 'polygon'])
        # Willekeurige grootte
        self.size = random.randint(10, 30)
        # Voor polygonen: lijst van punten genereren
        if self.shape_type == 'polygon':
            self.points = [(random.randint(-self.size, self.size), random.randint(-self.size, self.size)) for _ in range(5)]

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        # Als het puin volledig van het scherm is, reset hem
        if self.x < -self.size or self.y > HEIGHT:
            self.reset()

    def draw(self, surface):
        if self.shape_type == 'circle':
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.size // 2)
        elif self.shape_type == 'ellipse':
            # Ellips heeft een rect nodig
            pygame.draw.ellipse(surface, self.color, (int(self.x - self.size), int(self.y - self.size // 2), self.size * 2, self.size))
        elif self.shape_type == 'polygon':
            # Polygoon-punten transformeren naar de huidige x, y
            translated_points = [(self.x + px, self.y + py) for px, py in self.points]
            pygame.draw.polygon(surface, self.color, translated_points)

# --- 2. PUIN AANMAKEN ---
num_debris = 15
debris_list = [Debris() for _ in range(num_debris)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BG_COLOR)

    # --- 3. PUIN UPDATEN EN TEKENEN ---
    for debri in debris_list:
        debri.update()
        debri.draw(screen)

    # --- 4. TEKST INDICATOR ---
    text = font.render("SATURNUS - RUIMTEPUIN ACTIEF", True, TEXT_COLOR)
    text_bg = font.render("SATURNUS - RUIMTEPUIN ACTIEF", True, (0, 0, 0))
    screen.blit(text_bg, (WIDTH // 2 - text.get_width() // 2 + 2, HEIGHT // 2 + 2))
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))

    pygame.display.flip()
    clock.tick(60)
#---------------------------------------------------------------------------------------------------------------
#Verborgen Sterren & Onderdelen (Illustraties):
import pygame
import sys

# Initialisatie
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Geïsoleerd Effect: Glimmende Bonus Ster")
clock = pygame.time.Clock()

# Kleuren
BG_COLOR = (10, 15, 30)
STAR_GOLD = (255, 215, 0)
STAR_WHITE = (255, 255, 220)
TEXT_COLOR = (255, 255, 255)

font = pygame.font.Font(None, 36)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BG_COLOR)
    
    # Middelpunt voor de ster
    cx, cy = WIDTH // 2, HEIGHT // 2
    
    # --- 1. DE BONUS STER TEKENEN ---
    # A. Energie-gloed achter de ster (transparante cirkel via een extra Surface)
    glow_surface = pygame.Surface((150, 150), pygame.SRCALPHA)
    # Zachte goudkleurige gloed
    pygame.draw.circle(glow_surface, (255, 215, 0, 40), (75, 75), 70)
    screen.blit(glow_surface, (cx - 75, cy - 75))

    # B. De Ster zelf (Polygoon)
    star_points = [
        (cx, cy - 50),     # Bovenste punt
        (cx + 15, cy - 15),
        (cx + 50, cy - 10), # Rechter punt
        (cx + 20, cy + 15),
        (cx + 30, cy + 50), # Rechteronder punt
        (cx, cy + 30),      # Onderste punt
        (cx - 30, cy + 50), # Linkeronder punt
        (cx - 20, cy + 15),
        (cx - 50, cy - 10), # Linker punt
        (cx - 15, cy - 15)
    ]
    pygame.draw.polygon(screen, STAR_GOLD, star_points)
    
    # C. De glimmende kern (Witte kern cirkel)
    pygame.draw.circle(screen, STAR_WHITE, (cx, cy), 12)
    # Dunner goudkleurig detail op de kern
    pygame.draw.circle(screen, (255, 255, 0), (cx, cy), 8, 2)

    # --- 2. TEKST INDICATOR ---
    text = font.render("VERBORGEN STER - BONUS GEVONDEN!", True, TEXT_COLOR)
    text_bg = font.render("VERBORGEN STER - BONUS GEVONDEN!", True, (0, 0, 0))
    screen.blit(text_bg, (WIDTH // 2 - text.get_width() // 2 + 2, cy + 82))
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, cy + 80))

    pygame.display.flip()
    clock.tick(60)
#---------------------------------------------------------------------------------------------------------------
#Een mooie glimmende Ster-illustratie (voor de bonus).
import pygame
import sys

# Initialisatie
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Geïsoleerd Effect: Glimmende Bonus Ster")
clock = pygame.time.Clock()

# Kleuren
BG_COLOR = (10, 15, 30)
STAR_GOLD = (255, 215, 0)
STAR_WHITE = (255, 255, 220)
TEXT_COLOR = (255, 255, 255)

font = pygame.font.Font(None, 36)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BG_COLOR)
    
    # Middelpunt voor de ster
    cx, cy = WIDTH // 2, HEIGHT // 2
    
    # --- 1. DE BONUS STER TEKENEN ---
    # A. Energie-gloed achter de ster (transparante cirkel via een extra Surface)
    glow_surface = pygame.Surface((150, 150), pygame.SRCALPHA)
    # Zachte goudkleurige gloed
    pygame.draw.circle(glow_surface, (255, 215, 0, 40), (75, 75), 70)
    screen.blit(glow_surface, (cx - 75, cy - 75))

    # B. De Ster zelf (Polygoon)
    star_points = [
        (cx, cy - 50),     # Bovenste punt
        (cx + 15, cy - 15),
        (cx + 50, cy - 10), # Rechter punt
        (cx + 20, cy + 15),
        (cx + 30, cy + 50), # Rechteronder punt
        (cx, cy + 30),      # Onderste punt
        (cx - 30, cy + 50), # Linkeronder punt
        (cx - 20, cy + 15),
        (cx - 50, cy - 10), # Linker punt
        (cx - 15, cy - 15)
    ]
    pygame.draw.polygon(screen, STAR_GOLD, star_points)
    
    # C. De glimmende kern (Witte kern cirkel)
    pygame.draw.circle(screen, STAR_WHITE, (cx, cy), 12)
    # Dunner goudkleurig detail op de kern
    pygame.draw.circle(screen, (255, 255, 0), (cx, cy), 8, 2)

    # --- 2. TEKST INDICATOR ---
    text = font.render("VERBORGEN STER - BONUS GEVONDEN!", True, TEXT_COLOR)
    text_bg = font.render("VERBORGEN STER - BONUS GEVONDEN!", True, (0, 0, 0))
    screen.blit(text_bg, (WIDTH // 2 - text.get_width() // 2 + 2, cy + 82))
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, cy + 80))

    pygame.display.flip()
    clock.tick(60)
#---------------------------------------------------------------------------------------------------------------
#Illustraties voor de 7 unieke onderdelen (zoals de Heat stabilizer of de Cryo regulation core) die verschijnen als je het level wint.
import pygame
import sys
import random

# Initialisatie
pygame.init()
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Geïsoleerd Effect: Unieke Onderdelen Illustraties")
clock = pygame.time.Clock()

# Kleuren
BG_COLOR = (10, 15, 30)
TEXT_COLOR = (200, 220, 255)

font = pygame.font.Font(None, 24)
title_font = pygame.font.Font(None, 36)

# --- 1. DATA VOOR ONDERDELEN ---
PARTS = [
    {"name": "Heat stabilizer",      "color": (255, 100, 0), "type": "circle_glow", "x": 100},
    {"name": "Cryo regulation core", "color": (100, 255, 255), "type": "ice_core",    "x": 220},
    {"name": "Ion engine",           "color": (150, 50, 200), "type": "rect_power",   "x": 340},
    {"name": "Gravity shield",       "color": (50, 150, 255), "type": "polygon_shield", "x": 480},
    {"name": "Plasma injector",      "color": (255, 50, 50),  "type": "fire_power",     "x": 600},
    {"name": "Dampkring restorer",   "color": (0, 200, 255), "type": "glow_box",      "x": 740},
    {"name": "Fusion reactor",       "color": (0, 255, 150), "type": "core_power",     "x": 880}
]

def draw_part(part, surface):
    px, py = part["x"], 300
    size = 40
    color = part["color"]
    
    # Maak een temp surface met alpha-kanaal voor transparantie
    temp_surface = pygame.Surface((size*2+20, size*2+20), pygame.SRCALPHA)
    t_cx, t_cy = size+10, size+10

    # A. Energie-gloed achter de onderdelen (transparante cirkel)
    pygame.draw.circle(temp_surface, (*color, 60), (t_cx, t_cy), size)
    
    # B. Onderdeel-type specifieke visualisatie
    if part["type"] == "circle_glow":
        pygame.draw.circle(temp_surface, color, (t_cx, t_cy), size // 2)
        pygame.draw.circle(temp_surface, (255, 255, 255), (t_cx, t_cy), size // 3) # kern
    elif part["type"] == "ice_core":
        # Ijs-core (Polygoon)
        ice_points = [(t_cx, t_cy - size//2), (t_cx + size//3, t_cy), (t_cx, t_cy + size//2), (t_cx - size//3, t_cy)]
        pygame.draw.polygon(temp_surface, color, ice_points)
        pygame.draw.circle(temp_surface, (255, 255, 255), (t_cx, t_cy), size // 4) # kern
    elif part["type"] == "rect_power":
        # Ion engine (Twee rechthoeken)
        pygame.draw.rect(temp_surface, color, (t_cx - size//2, t_cy - size//3, size, size//1.5), border_radius=5)
        pygame.draw.rect(temp_surface, (255, 255, 255), (t_cx - size//3, t_cy - size//4, size//1.5, size//2), border_radius=3)
    elif part["type"] == "polygon_shield":
        # Gravity shield (Polygoon-schild)
        shield_points = [(t_cx - size//2, t_cy - size//3), (t_cx + size//2, t_cy - size//3), (t_cx + size//2, t_cy + size//3), (t_cx, t_cy + size//2), (t_cx - size//2, t_cy + size//3)]
        pygame.draw.polygon(temp_surface, color, shield_points)
        pygame.draw.circle(temp_surface, (255, 255, 255), (t_cx, t_cy), size // 4) # kern
    elif part["type"] == "fire_power":
        # Plasma injector (Driehoek)
        pygame.draw.polygon(temp_surface, color, [(t_cx - size//2, t_cy + size//2), (t_cx + size//2, t_cy + size//2), (t_cx, t_cy - size//2)])
        pygame.draw.circle(temp_surface, (255, 255, 255), (t_cx, t_cy + size//4), size // 4) # kern
    elif part["type"] == "glow_box":
        # Dampkring restorer (Gloeiende rechthoek)
        pygame.draw.rect(temp_surface, color, (t_cx - size//2, t_cy - size//2, size, size), border_radius=8, width=5)
        pygame.draw.circle(temp_surface, color, (t_cx, t_cy), size // 4) # kern
    elif part["type"] == "core_power":
        # Fusion reactor (Cirkel met lijnen)
        pygame.draw.circle(temp_surface, color, (t_cx, t_cy), size // 2, width=3)
        pygame.draw.circle(temp_surface, color, (t_cx, t_cy), size // 4) # kern
        pygame.draw.line(temp_surface, color, (t_cx - size//2, t_cy), (t_cx + size//2, t_cy), 3)
        pygame.draw.line(temp_surface, color, (t_cx, t_cy - size//2), (t_cx, t_cy + size//2), 3)

    # Zet de temp surface op het hoofdscherm
    surface.blit(temp_surface, (px - t_cx, py - t_cy))

    # C. Naam van het onderdeel onder het onderdeel
    name_text = font.render(part["name"], True, (200, 220, 255))
    surface.blit(name_text, (px - name_text.get_width() // 2, py + size + 10))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BG_COLOR)

    # --- 2. TITELS TEKENEN ---
    title_text = title_font.render("UNIEKE ONDERDELEN - LEVEL GEWONNEN!", True, (255, 255, 255))
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 100))

    # --- 3. ONDERDELEN TEKENEN ---
    for part in PARTS:
        draw_part(part, screen)

    pygame.display.flip()
    clock.tick(60)
#---------------------------------------------------------------------------------------------------------------
#De Eind-Cutscene: Een opeenvolging van 2 of 3 simpele illustraties die laten zien hoe de onderdelen samenkomen en de dampkring (een blauwe gloed rond de aarde) hersteld wordt.
import pygame
import sys

# Initialisatie
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Geïsoleerd Effect: Eind-Cutscene")
clock = pygame.time.Clock()

# Kleuren
BG_COLOR = (5, 10, 20)       # Diepe ruimte
SHIP_COLOR = (200, 200, 220)
EARTH_BLUE = (50, 130, 225)
EARTH_GREEN = (60, 180, 100)
TEXT_COLOR = (255, 255, 255)
DAMPKRING_COLOR = (0, 200, 255)

font = pygame.font.Font(None, 24)
title_font = pygame.font.Font(None, 36)

# Status variabele om de fases van de cutscene te timen
current_phase = 1
start_time = pygame.time.get_ticks()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BG_COLOR)
    
    # Middelpunten
    cx, cy = WIDTH // 2, HEIGHT // 2
    
    current_time = pygame.time.get_ticks()

    # --- FASES VAN DE CUTSCENE TIMEN ---
    # Elke 4000 milliseconden een nieuwe fase
    if current_time - start_time > 12000:
        # Cutscene voorbij, resetten of stoppen
        start_time = current_time
        current_phase = 1
    elif current_time - start_time > 8000:
        current_phase = 3 # Fase 3: Aarde Hersteld
    elif current_time - start_time > 4000:
        current_phase = 2 # Fase 2: Dampkring herstellen

    # --- 1. DE CUTSCENE FASES TEKENEN ---
    if current_phase == 1:
        # FASE 1: Onderdelen vliegen samen (Mechanische Formen vliegen naar het schip)
        phase_text = title_font.render("ONDERDELEN VERZAMELD - HET SCHIP HERSTELT DE DAMPKRING", True, (255, 255, 255))
        screen.blit(phase_text, (WIDTH // 2 - phase_text.get_width() // 2, 80))
        
        # Schip in het midden
        pygame.draw.polygon(screen, SHIP_COLOR, [(cx, cy - 80), (cx - 40, cy + 60), (cx + 40, cy + 60)])
        pygame.draw.circle(screen, (0, 180, 255), (cx, cy - 50), 10) # cockpit
        
        # Onderdelen vliegen naar het schip
        time_factor = (current_time - start_time) / 4000.0
        dist = 200 * (1 - time_factor) # Onderdelen vliegen dichterbij
        num_parts = 7
        for i in range(num_parts):
            angle = i * (360 / num_parts)
            # Bereken positie van het onderdeel
            part_x = cx + dist * pygame.math.Vector2(1, 0).rotate(angle).x
            part_y = cy + dist * pygame.math.Vector2(1, 0).rotate(angle).y
            # Willekeurig gekleurde cirkels als onderdelen
            pygame.draw.circle(screen, (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)), (int(part_x), int(part_y)), 15)

    elif current_phase == 2:
        # FASE 2: Dampkring herstellen (Schip herstelt dampkring rond de aarde)
        phase_text = title_font.render("DAMPKRING RESTORER ACTIEF", True, (255, 255, 255))
        screen.blit(phase_text, (WIDTH // 2 - phase_text.get_width() // 2, 80))
        
        # Schip boven de Aarde
        pygame.draw.polygon(screen, SHIP_COLOR, [(cx, cy - 180), (cx - 40, cy - 40), (cx + 40, cy - 40)])
        pygame.draw.circle(screen, (0, 180, 255), (cx, cy - 150), 10) # cockpit
        
        # Aarde in het midden
        pygame.draw.circle(screen, EARTH_BLUE, (cx, cy), 150)
        # Simpele continenten
        pygame.draw.ellipse(screen, EARTH_GREEN, (cx - 80, cy - 70, 70, 50))
        pygame.draw.ellipse(screen, EARTH_GREEN, (cx + 10, cy - 40, 90, 60))
        pygame.draw.polygon(screen, EARTH_GREEN, [(cx - 60, cy + 10), (cx - 10, cy + 80), (cx - 90, cy + 40)])
        pygame.draw.polygon(screen, EARTH_GREEN, [(cx + 20, cy + 30), (cx + 70, cy + 70), (cx + 80, cy + 20)])
        
        # De herstellende Dampkring (Zachte blauwe gloed)
        time_factor = (current_time - start_time - 4000) / 4000.0
        num_glow = 8
        for i in range(num_glow):
            # Zachte blauwe gloed
            pygame.draw.circle(screen, DAMPKRING_COLOR, (cx, cy), 150 + i * (5 * time_factor), 3)

    elif current_phase == 3:
        # FASE 3: Aarde Hersteld (Schip vliegt weg, herstelde dampkring)
        phase_text = title_font.render("AARDE HERSTELD - DE TOEKOMST IS VEILIG", True, (255, 255, 255))
        screen.blit(phase_text, (WIDTH // 2 - phase_text.get_width() // 2, 80))
        
        # Aarde in het midden met herstelde dampkring (Blauwe gloed)
        pygame.draw.circle(screen, EARTH_BLUE, (cx, cy), 150)
        # Simpele continenten
        pygame.draw.ellipse(screen, EARTH_GREEN, (cx - 80, cy - 70, 70, 50))
        pygame.draw.ellipse(screen, EARTH_GREEN, (cx + 10, cy - 40, 90, 60))
        pygame.draw.polygon(screen, EARTH_GREEN, [(cx - 60, cy + 10), (cx - 10, cy + 80), (cx - 90, cy + 40)])
        pygame.draw.polygon(screen, EARTH_GREEN, [(cx + 20, cy + 30), (cx + 70, cy + 70), (cx + 80, cy + 20)])
        
        # Herstelde Dampkring (Duidelijke blauwe gloed)
        pygame.draw.circle(screen, DAMPKRING_COLOR, (cx, cy), 150 + 5, 5) # Kern-gloed
        
        # Schip vliegt weg (linksboven, buiten beeld)
        time_factor = (current_time - start_time - 8000) / 4000.0
        ship_dist = 400 * time_factor # Schip vliegt verder weg
        pygame.draw.polygon(screen, SHIP_COLOR, [(cx - ship_dist, cy - ship_dist - 80), (cx - ship_dist - 40, cy - ship_dist + 60), (cx - ship_dist + 40, cy - ship_dist + 60)])
        pygame.draw.circle(screen, (0, 180, 255), (cx - ship_dist, cy - ship_dist - 50), 10) # cockpit

    # --- 2. TEKST INDICATOR ---
    phase_counter_text = font.render(f"Fase {current_phase} / 3", True, (200, 220, 255))
    screen.blit(phase_counter_text, (20, 20))

    pygame.display.flip()
    clock.tick(60)
#---------------------------------------------------------------------------------------------------------------