import pygame, sys
import math
from pygame.locals import *
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 1000))
pygame.display.set_caption("Save the Atmosphere - Ultimate Arcade Edition")
clock = pygame.time.Clock()

pygame.font.init()
titel_font = pygame.font.SysFont("Courier New", 45, bold=True)
knop_font = pygame.font.SysFont("Courier New", 30, bold=True)
uitleg_font = pygame.font.SysFont("Courier New", 24)
naam_font = pygame.font.SysFont("Courier New", 22, bold=True)
esc_font = pygame.font.SysFont("Courier New", 16, bold=True)
pop_font = pygame.font.SysFont("Courier New", 16) 
alarm_font = pygame.font.SysFont("Courier New", 35, bold=True)
timer_font = pygame.font.SysFont("Courier New", 26, bold=True)
boost_font = pygame.font.SysFont("Courier New", 20, bold=True)

# --- CONFIGURATIE MENU & KNOPPEN ---
titel_y_positie = 300
knop_breedte = 200
knop_hoogte = 60
knop_x = (800 / 2) - (knop_breedte / 2) 
knop_y = 450 
knop_rect = pygame.Rect(knop_x, knop_y, knop_breedte, knop_hoogte) 

# Menu Knoppen (voor Failed & ESC)
retry_rect = pygame.Rect(250, 550, 140, 50)
leave_rect = pygame.Rect(410, 550, 140, 50)

# Systeem variabelen
huidig_scherm = "startscherm"
info_huidige_planeet = None 
planeet_klik_tijd = 0
uitleg_start_tijd = 0
winst_terugkeer_timer = 0.0
skip_intro = False
game_gepauzeerd = False

dt = 0
vaste_hoogte = 900
player_pos = pygame.Vector2(400, vaste_hoogte)

ster = ("Zon", "orange", 400, 500, 100)
planeten = [
    ("Mercurius", (140, 140, 145), 550, 300, 32),
    ("Venus", (225, 180, 100), 200, 600, 42),
    ("Mars", (195, 60, 40), 370, 200, 34),
    ("Jupiter", (210, 150, 110), 650, 700, 55),
    ("Saturnus", (220, 190, 140), 700, 120, 40),
    ("Uranus", (160, 220, 240), 70, 900, 38),
    ("Neptunus", (40, 90, 215), 80, 80, 38),
    ("Aarde", (40, 150, 230), 300, 750, 42)
]

verzameld_fragments = [] 
slot_geopend = False

# Confetti setup
confetti_deeltjes = []
for _ in range(100):
    confetti_deeltjes.append({
        "x": random.randint(0, 800),
        "y": random.randint(-1000, 0),
        "snelheid": random.uniform(2, 5),
        "kleur": random.choice([
            (255, 50, 50),
            (50, 255, 50),
            (50, 50, 255),
            (255, 255, 50),
            (255, 50, 255)
        ]),
        "grootte": random.randint(6, 12),
        "zwiep": random.uniform(0, 2)
    })
aliens_verslagen_teller = 0
boost_timer = 0.0

sterren_achtergrond = []
for _ in range(80):
    sterren_achtergrond.append((random.randint(0, 800), random.randint(0, 1000), random.choice([2, 3, 4])))

vallende_objecten = [] 
object_spawn_timer = 0 
level_completed = False
fragment_pos = None 

huidige_levens = 3
alien_kogels = []
invincible_timer = 0
bevroren_timer = 0

speler_kogels = []
schoten_teller = 0
venus_explosie_center = None  # Veranderd naar center-punt voor mooiere cirkel/blok berekening
venus_explosie_timer = 0
venus_max_duur = 1.5

mercurius_wave_timer = 0
mercurius_wave_actief = False
jupiter_bliksem_timer = 0
jupiter_bliksem_x = None
jupiter_bliksem_zichtbaar = 0

neptunus_wind_timer = 0
neptunus_huidige_snelheid = 400

mars_storm_timers = []
mars_storm_actief = False
mars_storm_duur = 0.0
mars_zandkorrels = []

def reset_level(naam, direct_starten=False):
    global vallende_objecten, alien_kogels, speler_kogels, object_spawn_timer, invincible_timer
    global bevroren_timer, schoten_teller, venus_explosie_center, jupiter_bliksem_timer, jupiter_bliksem_x
    global huidige_levens, level_completed, fragment_pos, aliens_verslagen_teller, boost_timer
    global mars_storm_timers, mars_storm_actief, mars_storm_duur, mars_zandkorrels, planeet_klik_tijd, skip_intro, game_gepauzeerd
    
    vallende_objecten = []
    alien_kogels = []
    speler_kogels = []
    object_spawn_timer = 0
    invincible_timer = 0
    bevroren_timer = 0
    schoten_teller = 0
    venus_explosie_center = None
    jupiter_bliksem_timer = 0
    jupiter_bliksem_x = None
    huidige_levens = 3
    level_completed = False
    fragment_pos = None
    aliens_verslagen_teller = 0
    boost_timer = 0.0
    player_pos.x = 400
    game_gepauzeerd = False
    
    mars_storm_timers = [random.randint(10, 40), random.randint(45, 75)]
    mars_storm_actief = False
    mars_storm_duur = 0.0
    mars_zandkorrels = []
    
    if direct_starten:
        planeet_klik_tijd = pygame.time.get_ticks() - 21000
        skip_intro = True
    else:
        planeet_klik_tijd = pygame.time.get_ticks()
        skip_intro = False

# --- PIXEL VISUALS DRAWING ---

def teken_pixel_planeet(scherm, naam, cx, cy, r):
    x, y = int(cx), int(cy)
    if naam == "Mercurius":
        pygame.draw.circle(scherm, (130, 130, 135), (x, y), r)
        pygame.draw.rect(scherm, (90, 90, 95), (x - 12, y - 8, 8, 8))
        pygame.draw.rect(scherm, (90, 90, 95), (x + 10, y + 12, 6, 6))
    elif naam == "Venus":
        pygame.draw.circle(scherm, (230, 170, 70), (x, y), r)
        pygame.draw.rect(scherm, (190, 110, 30), (x - r + 4, y - 12, r*2 - 8, 6))
        pygame.draw.rect(scherm, (255, 210, 110), (x - r + 8, y + 4, r*2 - 16, 6))
    elif naam == "Mars":
        pygame.draw.circle(scherm, (180, 50, 35), (x, y), r)
        pygame.draw.rect(scherm, (255, 240, 240), (x - 8, y - r + 1, 16, 4))
        pygame.draw.rect(scherm, (110, 30, 20), (x - 16, y - 2, 24, 8))
    elif naam == "Jupiter":
        pygame.draw.circle(scherm, (220, 160, 110), (x, y), r)
        pygame.draw.rect(scherm, (160, 100, 60), (x - r + 3, y - 24, r*2 - 6, 8))
        pygame.draw.rect(scherm, (190, 40, 30), (x + 12, y + 2, 14, 8))
    elif naam == "Saturnus":
        pygame.draw.circle(scherm, (225, 200, 140), (x, y), r)
        pygame.draw.line(scherm, (200, 170, 110), (x - r - 25, y + 10), (x + r + 25, y - 10), 8)
        pygame.draw.line(scherm, (240, 220, 160), (x - r - 20, y + 8), (x + r + 20, y - 8), 4)
    elif naam == "Uranus":
        pygame.draw.circle(scherm, (150, 215, 230), (x, y), r)
        pygame.draw.rect(scherm, (200, 240, 250), (x - r + 10, y - 10, 14, 14))
    elif naam == "Neptunus":
        pygame.draw.circle(scherm, (35, 80, 200), (x, y), r)
        pygame.draw.rect(scherm, (15, 40, 130), (x - 16, y - 12, 12, 8))
    elif naam == "Aarde":
        pygame.draw.circle(scherm, (30, 110, 220), (x, y), r)
        pygame.draw.rect(scherm, (40, 160, 70), (x - 18, y - 20, 16, 14))
        pygame.draw.rect(scherm, (40, 160, 70), (x + 2, y - 8, 20, 12))
        pygame.draw.rect(scherm, (240, 240, 255), (x - 10, y - r + 6, 25, 4))

def teken_hangslot(scherm, cx, cy):
    x, y = int(cx), int(cy)
    pygame.draw.rect(scherm, (180, 180, 185), (x - 12, y - 24, 24, 12), 4)
    pygame.draw.rect(scherm, (240, 180, 20), (x - 18, y - 12, 36, 30))
    pygame.draw.rect(scherm, (0, 0, 0), (x - 4, y - 2, 8, 14))

def teken_pixel_alien_groot(scherm, cx, cy, kleur, planeet_naam):
    x, y = int(cx), int(cy)
    if planeet_naam in ["Mercurius", "Venus"]:
        pygame.draw.rect(scherm, kleur, (x - 28, y - 12, 56, 16))
        pygame.draw.rect(scherm, kleur, (x - 20, y + 4, 40, 12))
        pygame.draw.rect(scherm, (255, 255, 255), (x - 12, y - 4, 6, 6))
        pygame.draw.rect(scherm, (255, 255, 255), (x + 6, y - 4, 6, 6))
    elif planeet_naam in ["Mars", "Jupiter"]:
        pygame.draw.rect(scherm, kleur, (x - 24, y - 20, 48, 24))
        pygame.draw.rect(scherm, (0, 0, 0), (x - 14, y - 4, 6, 6))
        pygame.draw.rect(scherm, (0, 0, 0), (x + 8, y - 4, 6, 6))
        pygame.draw.rect(scherm, kleur, (x - 20, y + 4, 8, 16))
        pygame.draw.rect(scherm, kleur, (x + 12, y + 4, 8, 16))
    else:
        pygame.draw.rect(scherm, (40, 40, 45), (x - 32, y - 8, 64, 16))
        pygame.draw.rect(scherm, kleur, (x - 16, y - 16, 32, 24))
        pygame.draw.rect(scherm, (0, 255, 255), (x - 24, y + 8, 10, 8))
        pygame.draw.rect(scherm, (0, 255, 255), (x + 14, y + 8, 10, 8))

def teken_achtergrond_sterren(scherm):
    scherm.fill((5, 5, 12)) 
    tijd_flikker = pygame.time.get_ticks() // 250
    for i, s in enumerate(sterren_achtergrond):
        kleur = (255, 255, 255) if (i + tijd_flikker) % 3 != 0 else (150, 150, 200)
        pygame.draw.rect(scherm, kleur, (s[0], s[1], s[2], s[2]))

def teken_pixel_schip_mega(scherm, pos, invincible=False, frozen=False):
    if invincible and int(pygame.time.get_ticks() / 100) % 2 == 0:
        return
    x, y = int(pos.x), int(pos.y)
    base_color = (0, 230, 255) if frozen else (220, 220, 225)
    shadow_color = (0, 160, 200) if frozen else (140, 142, 150)
    
    # Vleugels en basisstructuur
    pygame.draw.rect(scherm, (130, 0, 0), (x - 36, y + 12, 72, 12))   
    pygame.draw.rect(scherm, (200, 0, 0), (x - 44, y, 8, 20))       
    pygame.draw.rect(scherm, (200, 0, 0), (x + 36, y, 8, 20))       
    pygame.draw.rect(scherm, base_color, (x - 12, y - 32, 24, 44))   
    pygame.draw.rect(scherm, shadow_color, (x - 12, y + 4, 24, 8))  
    pygame.draw.rect(scherm, base_color, (x - 20, y - 12, 40, 24))  
    pygame.draw.rect(scherm, (0, 100, 255), (x - 6, y - 18, 12, 16)) 
    
    # --- RETRO EN KRACHTIGE STRALEN ---
    if not frozen:
        # Linker motor straal
        h_links = random.choice([25, 35, 45])
        pygame.draw.rect(scherm, (255, 60, 0), (x - 32, y + 12, 6, h_links))
        pygame.draw.rect(scherm, (255, 150, 0), (x - 30, y + 12, 2, int(h_links * 0.7)))
        
        # Hoofdmotor straal (Midden)
        h_mid = random.choice([35, 50, 65])
        pygame.draw.rect(scherm, (255, 40, 0), (x - 6, y + 12, 12, h_mid))
        pygame.draw.rect(scherm, (255, 130, 0), (x - 4, y + 12, 8, int(h_mid * 0.7)))
        pygame.draw.rect(scherm, (255, 230, 0), (x - 2, y + 12, 4, int(h_mid * 0.4)))
        
        # Rechter motor straal
        h_rechts = random.choice([25, 35, 45])
        pygame.draw.rect(scherm, (255, 60, 0), (x + 26, y + 12, 6, h_rechts))
        pygame.draw.rect(scherm, (255, 150, 0), (x + 28, y + 12, 2, int(h_rechts * 0.7)))

def teken_pixel_boss_mega(scherm, cx, cy):
    x, y = int(cx), int(cy)
    pygame.draw.rect(scherm, (70, 0, 90), (x - 65, y - 15, 130, 30))    
    pygame.draw.rect(scherm, (110, 0, 140), (x - 45, y - 25, 90, 45))   
    pygame.draw.rect(scherm, (0, 255, 255), (x - 25, y - 40, 50, 18))   
    pygame.draw.rect(scherm, (200, 50, 0), (x - 60, y + 15, 16, 12))
    pygame.draw.rect(scherm, (200, 50, 0), (x + 44, y + 15, 16, 12))

def teken_pixel_rots_detail(scherm, cx, cy, straal, kleur):
    x, y = int(cx), int(cy)
    s = int(straal)
    pygame.draw.rect(scherm, kleur, (x - s, y - int(s*0.7), s*2, int(s*1.4)))
    pygame.draw.rect(scherm, kleur, (x - int(s*0.8), y - s, int(s*1.6), s*2))

def teken_pixel_kristal_detail(scherm, cx, cy, straal):
    x, y = int(cx), int(cy)
    s = int(straal)
    pygame.draw.rect(scherm, (0, 190, 255), (x - 6, y - s, 12, s * 2))  
    pygame.draw.rect(scherm, (0, 190, 255), (x - s, y - 6, s * 2, 12))  

def teken_pixel_fragment_prijs(scherm, cx, cy, kleur):
    x, y = int(cx), int(cy)
    pygame.draw.rect(scherm, kleur, (x - 20, y - 20, 40, 40))
    pygame.draw.rect(scherm, (255, 255, 255), (x - 14, y - 14, 28, 28)) 

# --- GLOEDNIEUWE RETRO ARCADE EXPLOSIE TEKEN FUNCTIE ---
def teken_retro_explosie(scherm, cx, cy, resterende_tijd):
    # Bereken hoe ver de explosie is (0.0 tot 1.0)
    voortgang = (venus_max_duur - resterende_tijd) / venus_max_duur
    
    # Maximale grootte van de schokgolf
    max_straal = 80
    huidige_grootte = int(voortgang * max_straal)
    
    if huidige_grootte < 5:
        return

    # Retro blokken-lagen tekenen (van buiten naar binnen)
    # 1. Buitenste rode laag
    r1 = huidige_grootte
    pygame.draw.rect(scherm, (220, 20, 0), (cx - r1, cy - r1, r1 * 2, r1 * 2), int(8 * (1 - voortgang)) + 2)
    
    # 2. Middelste oranje laag (loopt iets achter in grootte)
    if voortgang < 0.8:
        r2 = int(huidige_grootte * 0.7)
        pygame.draw.rect(scherm, (255, 110, 0), (cx - r2, cy - r2, r2 * 2, r2 * 2))
        
    # 3. Hete gele/witte kern (verdwijnt snel aan het einde)
    if voortgang < 0.5:
        r3 = int(huidige_grootte * 0.4)
        pygame.draw.rect(scherm, (255, 240, 100), (cx - r3, cy - r3, r3 * 2, r3 * 2))

    # 4. Extra willekeurige pixel-flarden rondom de explosie voor de retro-vibe
    random.seed(int(cx + cy)) # Zorgt dat de flarden stabiel exploderen
    for _ in range(12):
        afstand = random.randint(int(huidige_grootte * 0.5), huidige_grootte + 15)
        hoek = random.uniform(0, math.pi * 2)
        px = int(cx + math.cos(hoek) * afstand)
        py = int(cy + math.sin(hoek) * afstand)
        p_grootte = random.randint(4, 10)
        p_kleur = random.choice([(255, 60, 0), (255, 160, 0), (200, 0, 0)])
        pygame.draw.rect(scherm, p_kleur, (px, py, p_grootte, p_grootte))

# Configurations
planeet_instellingen = {
    "Mercurius": {"alien_kleur": (200, 100, 40), "gevaar_kleur": (190, 20, 20), "frag_kleur": (255, 215, 0)},
    "Venus": {"alien_kleur": (255, 230, 100), "gevaar_kleur": (40, 150, 40), "frag_kleur": (255, 0, 255)},
    "Mars": {"alien_kleur": (255, 50, 50), "gevaar_kleur": (110, 110, 115), "frag_kleur": (255, 90, 0)},
    "Jupiter": {"alien_kleur": (230, 180, 140), "gevaar_kleur": (0, 230, 255), "frag_kleur": (255, 255, 0)},
    "Saturnus": {"alien_kleur": (160, 140, 90), "gevaar_kleur": (170, 170, 180), "frag_kleur": (230, 220, 130)},
    "Uranus": {"alien_kleur": (140, 220, 230), "gevaar_kleur": (160, 210, 240), "frag_kleur": (0, 255, 255)},
    "Neptunus": {"alien_kleur": (40, 80, 255), "gevaar_kleur": (140, 20, 150), "frag_kleur": (30, 100, 255)}
}

planeten_teksten = {
    "Venus": ["Venus: Every 5 shots triggers a random", "explosion somewhere on the screen. Stay away!"],
    "Mars": ["Mars: Watch out for giant debris", "and sudden, intense sandstorms!"],
    "Jupiter": ["Jupiter: Beware of random, powerful", "lightning strikes shooting from the sky."],
    "Saturnus": ["Saturnus: The rings are breaking apart! Giant debris", "and slow, powerful Alien Motherships attack!"],
    "Uranus": ["Uranus: Beautiful ice crystals fall from the sky.", "Snowballs freeze you for 5 seconds!"],
    "Neptunus": ["Neptunus: Alien lasers freeze you for 3 seconds.", "The extreme wind constantly changes your speed!"],
    "Mercurius": ["Mercurius: Extreme heat! Every minute,", "a massive wave of aliens attacks at once."]
}

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if huidig_scherm == "startscherm":
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                huidig_scherm = "uitleg_scherm"
                uitleg_start_tijd = pygame.time.get_ticks()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
                if knop_rect.collidepoint(event.pos):
                    huidig_scherm = "uitleg_scherm"
                    uitleg_start_tijd = pygame.time.get_ticks()
        
        elif huidig_scherm == "uitleg_scherm":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                tijd_op_uitleg = pygame.time.get_ticks() - uitleg_start_tijd
                if tijd_op_uitleg >= 38000: 
                    for planeet in planeten:
                        naam, kleur, x, y, grootte = planeet
                        if math.dist(event.pos, (x, y)) <= grootte:
                            if naam == "Aarde":
                                if len(verzameld_fragments) >= 7: 
                                    huidig_scherm = "witscherm"
                                continue

                            huidig_scherm = naam 
                            info_huidige_planeet = planeet 
                            reset_level(naam, direct_starten=False)
        
        elif huidig_scherm in [p[0] for p in planeten]:
            if huidige_levens <= 0 or game_gepauzeerd:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if retry_rect.collidepoint(event.pos):
                        reset_level(huidig_scherm, direct_starten=True)
                    elif leave_rect.collidepoint(event.pos):
                        huidig_scherm = "uitleg_scherm"
                        uitleg_start_tijd = pygame.time.get_ticks() - 38000
                
                if game_gepauzeerd and event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    game_gepauzeerd = False
            
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not level_completed:
                    if bevroren_timer <= 0:  
                        if boost_timer > 0 or len(speler_kogels) == 0:
                            speler_kogels.append(pygame.Vector2(player_pos.x, vaste_hoogte - 38))
                        
                        if huidig_scherm == "Venus":
                            schoten_teller += 1
                            if schoten_teller >= 5:
                                schoten_teller = 0
                                # Opslaan als een Vector2 centerpunt i.p.V. Rect voor retro-cirkel effecten
                                venus_explosie_center = pygame.Vector2(random.randint(100, 700), random.randint(200, 750))
                                venus_explosie_timer = venus_max_duur 

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    tijd_voorbij = pygame.time.get_ticks() - planeet_klik_tijd
                    if tijd_voorbij >= 21000 or skip_intro:
                        game_gepauzeerd = True

    if game_gepauzeerd:
        dt = 0
    else:
        dt = clock.tick(60) / 1000

    if invincible_timer > 0: invincible_timer -= dt
    if bevroren_timer > 0: bevroren_timer -= dt
    if venus_explosie_timer > 0: venus_explosie_timer -= dt
    if boost_timer > 0: boost_timer -= dt

    # DRAWING & LOGIC
    if huidig_scherm == "startscherm":
        teken_achtergrond_sterren(screen)
        titel_tekst = titel_font.render("SAVE THE ATMOSPHERE", True, (0, 255, 0)) 
        screen.blit(titel_tekst, ((800 / 2) - (titel_tekst.get_width() / 2), titel_y_positie))
        pygame.draw.rect(screen, (0, 255, 0), knop_rect, 4) 
        knop_tekst = knop_font.render("START", True, (0, 255, 0))
        screen.blit(knop_tekst, (knop_x + (knop_breedte / 2) - (knop_tekst.get_width() / 2), knop_y + (knop_hoogte / 2) - (knop_tekst.get_height() / 2))) 

    elif huidig_scherm == "uitleg_scherm":
        teken_achtergrond_sterren(screen)
        pygame.draw.circle(screen, ster[1], (ster[2], ster[3]), ster[4])
        
        for naam, kleur, x, y, grootte in planeten: 
            teken_pixel_planeet(screen, naam, x, y, grootte)
            if naam == "Aarde" and len(verzameld_fragments) < 7:
                teken_hangslot(screen, x, y)
                p_tekst = naam_font.render(f"LOCKED ({len(verzameld_fragments)}/7)", True, (255, 100, 100))
            else:
                vinkje = " [V]" if naam in verzameld_fragments else ""
                p_tekst = naam_font.render(naam + vinkje, True, (255, 255, 255)) 
            screen.blit(p_tekst, (x - (p_tekst.get_width() / 2), y - grootte - 25))

        tijd_op_uitleg = pygame.time.get_ticks() - uitleg_start_tijd
        if tijd_op_uitleg < 38000:
            teken_pixel_schip_mega(screen, pygame.Vector2(730, 915), invincible=False, frozen=False)
            
            # Witte tekstballon
            pygame.draw.rect(screen, "white", pygame.Rect(140, 840, 530, 120), border_radius=4)
            pygame.draw.polygon(screen, "white", [(655, 910), (655, 930), (685, 925)])
            
            if tijd_op_uitleg < 8000: actieve_tekst = ["ATTENTION PILOT: Earth is in danger!", "The Sun is destroying our atmosphere."]
            elif tijd_op_uitleg < 16000: actieve_tekst = ["HOW TO PLAY: Click a planet to start.", "Every world contains an atmospheric part."]
            elif tijd_op_uitleg < 24000: actieve_tekst = ["HOW TO PLAY:", "- Use the A en D keys to move around.", "-Press the space-key to shoot.", ]
            elif tijd_op_uitleg < 32000: actieve_tekst = ["- Avoid world specific hazards.", "- Gather all fragments to win.", "- Earth unlocks at 7 fragments.", ]
            else: actieve_tekst = ["Protect your ship at all costs.", "Good luck, captain. Save our planet!"]

            y_offset = 855
            for regel in actieve_tekst:
                screen.blit(pop_font.render(regel, True, "black"), (160, y_offset))
                y_offset += 22

    elif huidig_scherm == "witscherm":

        # Donkere wazige overlay
        teken_achtergrond_sterren(screen)

        blur_surface = pygame.Surface((800, 1000), pygame.SRCALPHA)
        blur_surface.fill((10, 15, 30, 200))
        screen.blit(blur_surface, (0, 0))

        # Confetti
        for p in confetti_deeltjes:
            p["y"] += p["snelheid"]
            p["x"] += math.sin(p["y"] * 0.05) * p["zwiep"]

            if p["y"] > 1000:
                p["y"] = random.randint(-50, -10)
                p["x"] = random.randint(0, 800)

            pygame.draw.rect(
                screen,
                p["kleur"],
                (int(p["x"]), int(p["y"]), p["grootte"], p["grootte"])
            )

        txt_line1 = titel_font.render(
            "MISSION ACCOMPLISHED!",
            True,
            (0, 255, 100)
        )

        txt_line2 = knop_font.render(
            "Earth's Atmosphere is Restored",
            True,
            (255, 255, 255)
        )

        txt_line3 = naam_font.render(
            "Thank you, Captain!",
            True,
            (0, 220, 255)
        )

        screen.blit(txt_line1, txt_line1.get_rect(center=(400, 450)))
        screen.blit(txt_line2, txt_line2.get_rect(center=(400, 520)))
        screen.blit(txt_line3, txt_line3.get_rect(center=(400, 580)))
        

    elif huidig_scherm in [p[0] for p in planeten]:
        if info_huidige_planeet:
            naam, kleur, x, y, grootte = info_huidige_planeet
            teken_achtergrond_sterren(screen)
            
            tijd_voorbij = pygame.time.get_ticks() - planeet_klik_tijd
            
            if tijd_voorbij < 5000 and not skip_intro:
                titel = titel_font.render(naam.upper(), True, (0, 255, 255))
                screen.blit(titel, titel.get_rect(center=(400, 500)))
            elif tijd_voorbij < 15000 and not skip_intro:
                teken_pixel_schip_mega(screen, pygame.Vector2(730, 915), invincible=False, frozen=False)
                
                pygame.draw.rect(screen, "white", pygame.Rect(140, 840, 530, 120), border_radius=4)
                pygame.draw.polygon(screen, "white", [(655, 910), (655, 930), (685, 925)])
                if naam in planeten_teksten:
                    y_offset = 855
                    for regel in planeten_teksten[naam]:
                        screen.blit(pop_font.render(regel, True, "black"), (160, y_offset))
                        y_offset += 22
            elif tijd_voorbij < 17000 and not skip_intro:
                pass 
            elif tijd_voorbij < 21000 and not skip_intro:
                status = "3" if tijd_voorbij < 18000 else "2" if tijd_voorbij < 19000 else "1" if tijd_voorbij < 20000 else "START!"
                screen.blit(titel_font.render(status, True, (0, 255, 0)), titel_font.render(status, True, (0, 255, 0)).get_rect(center=(400, 500)))
            else: 
                vliegtijd_seconden = (tijd_voorbij - 21000) / 1000 
                resterende_seconden = max(0, 90 - int(vliegtijd_seconden))
                minuten, seconden = resterende_seconden // 60, resterende_seconden % 60

                # --- GEAUTOMATISEERD GAME OVER MENU (FAILED) ---
                if huidige_levens <= 0:
                    fail_tekst = titel_font.render("YOU FAILED", True, (255, 0, 0))
                    screen.blit(fail_tekst, fail_tekst.get_rect(center=(400, 450)))
                    
                    pygame.draw.rect(screen, (0, 255, 0), retry_rect, 3, border_radius=4)
                    r_txt = knop_font.render("RETRY", True, (0, 255, 0))
                    screen.blit(r_txt, (retry_rect.x + (retry_rect.width/2) - (r_txt.get_width()/2), retry_rect.y + 10))
                    
                    pygame.draw.rect(screen, (255, 255, 255), leave_rect, 3, border_radius=4)
                    l_txt = knop_font.render("LEAVE", True, (255, 255, 255))
                    screen.blit(l_txt, (leave_rect.x + (leave_rect.width/2) - (l_txt.get_width()/2), leave_rect.y + 10))

                # --- ESC/PAUZE MENU ---
                elif game_gepauzeerd:
                    pygame.draw.rect(screen, (0, 255, 0), retry_rect, 3, border_radius=4)
                    r_txt = knop_font.render("RETRY", True, (0, 255, 0))
                    screen.blit(r_txt, (retry_rect.x + (retry_rect.width/2) - (r_txt.get_width()/2), retry_rect.y + 10))
                    
                    pygame.draw.rect(screen, (255, 255, 255), leave_rect, 3, border_radius=4)
                    l_txt = knop_font.render("LEAVE", True, (255, 255, 255))
                    screen.blit(l_txt, (leave_rect.x + (leave_rect.width/2) - (l_txt.get_width()/2), leave_rect.y + 10))

                # --- AUTOMATISCH TERUG NAAR ZONNESTELSEL BIJ WIN ---
                elif level_completed:
                    screen.blit(titel_font.render("LEVEL COMPLETED", True, (255, 215, 0)), titel_font.render("LEVEL COMPLETED", True, (255, 215, 0)).get_rect(center=(400, 500)))
                    winst_terugkeer_timer += dt
                    if winst_terugkeer_timer >= 4.0:
                        winst_terugkeer_timer = 0.0
                        huidig_scherm = "uitleg_scherm"
                        uitleg_start_tijd = pygame.time.get_ticks() - 38000 

                else: 
                    # ARCADE UI INFORMATIE
                    screen.blit(timer_font.render(f"TIME: {minuten:02d}:{seconden:02d}", True, (255, 255, 0)), (20, 40))
                    screen.blit(timer_font.render(f"ALIENS: {aliens_verslagen_teller}/10", True, (0, 255, 255)), (20, 75))
                    
                    if boost_timer > 0:
                        if (pygame.time.get_ticks() // 150) % 2 == 0:
                            flits_kleur = (255, 69, 0) if (pygame.time.get_ticks() // 150) % 4 == 0 else (255, 0, 0)
                            screen.blit(boost_font.render("YOU GAIN A BOOST!", True, flits_kleur), (20, 110))

                    # --- VENUS EXPLOSIE MECHANISME (GEFIXT EN VERBETERD NAAR RETRO) ---
                    if naam == "Venus" and venus_explosie_timer > 0 and venus_explosie_center is not None:
                        # Teken de brute nieuwe retro pixel-explosie!
                        teken_retro_explosie(screen, venus_explosie_center.x, venus_explosie_center.y, venus_explosie_timer)
                        
                        # Schade berekenen op basis van de huidige explosie-straal (tot max 80 pixels)
                        voortgang = (venus_max_duur - venus_explosie_timer) / venus_max_duur
                        huidige_straal = voortgang * 80
                        
                        if invincible_timer <= 0 and math.dist((venus_explosie_center.x, venus_explosie_center.y), (player_pos.x, vaste_hoogte)) < (huidige_straal + 25):
                            huidige_levens -= 1
                            invincible_timer = 5.0

                    # --- MARS ZANDSTORM ---
                    if naam == "Mars" and resterende_seconden > 0:
                        for t in mars_storm_timers[:]:
                            if int(vliegtijd_seconden) == t and not mars_storm_actief:
                                mars_storm_actief = True
                                mars_storm_duur = 6.0
                                mars_storm_timers.remove(t)
                                for _ in range(150):
                                    mars_zandkorrels.append([random.randint(800, 1200), random.randint(0, 1000), random.randint(400, 700)])

                        if mars_storm_actief:
                            mars_storm_duur -= dt
                            if mars_storm_duur <= 0:
                                mars_storm_actief = False
                            overlay = pygame.Surface((800, 1000), pygame.SRCALPHA)
                            overlay.fill((235, 210, 80, 130)) 
                            screen.blit(overlay, (0,0))

                            for korrel in mars_zandkorrels:
                                korrel[0] -= korrel[2] * dt
                                pygame.draw.rect(screen, (255, 255, 140), (int(korrel[0]), int(korrel[1]), 5, 5))
                                if korrel[0] < -20:
                                    korrel[0] = random.randint(800, 900)
                                    korrel[1] = random.randint(0, 1000)

                    # --- JUPITER BLIKSEM ---
                    if naam == "Jupiter" and resterende_seconden > 0:
                        jupiter_bliksem_timer += dt
                        if jupiter_bliksem_timer >= 4.0: 
                            jupiter_bliksem_timer = 0
                            jupiter_bliksem_x = random.randint(50, 750)
                            jupiter_bliksem_zichtbaar = 0.4 
                        if jupiter_bliksem_zichtbaar > 0 and jupiter_bliksem_x is not None:
                            jupiter_bliksem_zichtbaar -= dt
                            pygame.draw.lines(screen, "cyan", False, [(jupiter_bliksem_x, 0), (jupiter_bliksem_x - 40, 350), (jupiter_bliksem_x + 40, 650), (jupiter_bliksem_x, 1000)], 8)
                            if invincible_timer <= 0 and abs(player_pos.x - jupiter_bliksem_x) < 45:
                                huidige_levens -= 1
                                invincible_timer = 5.0

                    # --- NEPTUNUS WIND ---
                    if naam == "Neptunus":
                        neptunus_wind_timer += dt
                        if neptunus_wind_timer >= 2.0: 
                            neptunus_wind_timer = 0
                            neptunus_huidige_snelheid = random.choice([150, 650]) 
                    else:
                        neptunus_huidige_snelheid = 400 if naam != "Uranus" else 200

                    # --- BESTURING & SCHIP TEKENEN ---
                    if bevroren_timer <= 0:
                        knoppen = pygame.key.get_pressed()

                    if knoppen[pygame.K_a] or knoppen[pygame.K_LEFT]:
                        player_pos.x -= neptunus_huidige_snelheid * dt

                    if knoppen[pygame.K_d] or knoppen[pygame.K_RIGHT]:
                        player_pos.x += neptunus_huidige_snelheid * dt

                    # Mars zandstorm duwt schip naar links
                    if naam == "Mars" and mars_storm_actief:
                        player_pos.x -= 250 * dt

                    player_pos.x = max(45, min(player_pos.x, 755)) 

                    teken_pixel_schip_mega(screen, player_pos, invincible_timer > 0, bevroren_timer > 0)

                    # --- BEWEEG SPELER KOGELS ---
                    for pk in speler_kogels[:]:
                        pk.y -= 850 * dt
                        if boost_timer > 0:
                            pygame.draw.rect(screen, (0, 255, 100), (int(pk.x) - 8, int(pk.y), 16, 28))
                            pygame.draw.rect(screen, (255, 255, 255), (int(pk.x) - 4, int(pk.y + 4), 8, 20))
                        else:
                            pygame.draw.rect(screen, (255, 255, 0), (int(pk.x) - 4, int(pk.y), 8, 24))
                            pygame.draw.rect(screen, (255, 255, 255), (int(pk.x) - 2, int(pk.y + 4), 4, 16))
                        if pk.y < 0: speler_kogels.remove(pk)

                    # --- SPAWN LOGICA OBJECTEN ---
                    if resterende_seconden > 0:
                        base_interval = 850 if naam == "Saturnus" else 1100
                        spawn_interval = max(350 if naam == "Saturnus" else 220, base_interval - int(vliegtijd_seconden * 5))

                        object_spawn_timer += dt * 1000
                        if object_spawn_timer >= spawn_interval:
                            object_spawn_timer = 0
                            spawn_x = random.randint(50, 750)
                            instellingen = planeet_instellingen.get(naam, {"alien_kleur": (255, 255, 255), "gevaar_kleur": (200, 0, 0)})

                            if naam == "Saturnus":
                                type_object = random.choice(["gevaar", "gevaar", "grote_alien", "alien"])
                            else:
                                type_object = random.choice(["alien", "gevaar"])

                            if type_object == "gevaar":
                                if naam == "Saturnus": grootte_obj = random.randint(45, 75)
                                elif naam == "Mars": grootte_obj = random.randint(35, 65)
                                elif naam == "Uranus": grootte_obj = random.randint(32, 55)
                                else: grootte_obj = 28
                                
                                sub_type = "sneeuwbal" if (naam == "Uranus" and random.random() > 0.5) else "kristal" if naam == "Uranus" else "rots"
                                vallende_objecten.append([spawn_x, -50, "gevaar", instellingen["gevaar_kleur"], grootte_obj, sub_type, random.randint(180, 320), 0, 0])
                            
                            elif type_object == "grote_alien":
                                heading = random.choice([-1, 1])
                                vallende_objecten.append([spawn_x, -60, "grote_alien", "darkred", 55, "boss", random.randint(50, 80), 0, heading])
                            
                            else: 
                                vallende_objecten.append([spawn_x, -40, "alien", instellingen["alien_kleur"], 32, "alien", random.randint(130, 220), random.randint(0, 1000), 0])

                        # --- ALIEN SCHIET LOGICA ---
                        for obj in vallende_objecten:
                            if 0 < obj[1] < 750:
                                if obj[2] == "alien":
                                    obj[7] += dt * 1000
                                    if obj[7] >= 1700:
                                        obj[7] = 0
                                        alien_kogels.append([obj[0], obj[1] + obj[4], False]) 
                                elif obj[2] == "grote_alien":
                                    obj[7] += dt * 1000
                                    if obj[7] >= 900: 
                                        obj[7] = 0
                                        alien_kogels.append([obj[0], obj[1] + obj[4], True]) 

                    # Fragment landing (Einde level)
                    else: 
                        if fragment_pos is None: fragment_pos = pygame.Vector2(400, -50)
                        fragment_pos.y += 120 * dt
                        inst = planeet_instellingen.get(naam, {"frag_kleur": (255, 215, 0)})
                        
                        teken_pixel_fragment_prijs(screen, fragment_pos.x, fragment_pos.y, inst["frag_kleur"])
                        if math.dist((fragment_pos.x, fragment_pos.y), (player_pos.x, vaste_hoogte)) < 45:
                            level_completed = True
                            if naam not in verzameld_fragments:
                                verzameld_fragments.append(naam)

                    # --- ALIEN LASERS BEWEGEN & CHECKEN ---
                    for kogel in alien_kogels[:]:
                        kogel[1] += (650 if kogel[2] else 500) * dt
                        l_lengte = 40 if kogel[2] else 18
                        l_breedte = 10 if kogel[2] else 5
                        pygame.draw.rect(screen, (255, 60, 0) if kogel[2] else (255, 0, 50), (int(kogel[0]) - int(l_breedte/2), int(kogel[1]), l_breedte, l_lengte))

                        # Check collision
                        if resterende_seconden > 0 and invincible_timer <= 0 and math.dist((kogel[0], kogel[1]), (player_pos.x, vaste_hoogte)) < 36:
                            huidige_levens -= 1
                            invincible_timer = 5.0
                            if naam == "Neptunus": bevroren_timer = 3.0
                            alien_kogels.remove(kogel)
                        elif kogel[1] > 1000: alien_kogels.remove(kogel)

                    # --- OBJECTEN BEWEGEN & TEKENEN ---
                    for obj in vallende_objecten[:]:
                        obj[1] += obj[6] * dt 

                        if obj[2] == "grote_alien":
                            obj[0] += 100 * obj[8] * dt 
                            if obj[0] < 70 or obj[0] > 730: 
                                obj[8] *= -1 

                        if obj[2] == "alien": 
                            teken_pixel_alien_groot(screen, obj[0], obj[1], obj[3], naam)
                        elif obj[2] == "grote_alien":
                            teken_pixel_boss_mega(screen, obj[0], obj[1])
                        else: 
                            if obj[5] == "sneeuwbal":
                                pygame.draw.rect(screen, (240, 240, 255), (obj[0] - obj[4], obj[1] - obj[4], obj[4]*2, obj[4]*2))
                            elif obj[5] == "kristal":
                                teken_pixel_kristal_detail(screen, obj[0], obj[1], obj[4])
                            else: 
                                teken_pixel_rots_detail(screen, obj[0], obj[1], obj[4], obj[3])

                        # Speler laser inslag check
                        for pk in speler_kogels[:]:
                            if math.dist((obj[0], obj[1]), (pk.x, pk.y)) < (obj[4] + 20):
                                if pk in speler_kogels: speler_kogels.remove(pk)
                                
                                if obj[2] in ["alien", "grote_alien"]:
                                    if boost_timer <= 0: 
                                        aliens_verslagen_teller += 1
                                        if aliens_verslagen_teller >= 10:
                                            aliens_verslagen_teller = 0
                                            boost_timer = 10.0 

                                if obj in vallende_objecten: vallende_objecten.remove(obj)
                                break

                        # Speler botsing met objecten
                        if invincible_timer <= 0 and math.dist((obj[0], obj[1]), (player_pos.x, vaste_hoogte)) < (obj[4] + 34):
                            if resterende_seconden > 0:
                                huidige_levens -= 1 
                                invincible_timer = 5.0
                                if obj[5] == "sneeuwbal": bevroren_timer = 5.0
                                if obj in vallende_objecten: vallende_objecten.remove(obj)
                            continue            

                        if obj[1] > 1050:
                            if obj in vallende_objecten: vallende_objecten.remove(obj)

                if huidige_levens > 0 and not game_gepauzeerd:
                    for i in range(huidige_levens):
                        hx = 750 - (i * 35)
                        hy = 20
                        pygame.draw.rect(screen, (255, 0, 0), (hx - 10, hy, 8, 6))
                        pygame.draw.rect(screen, (255, 0, 0), (hx + 2, hy, 8, 6))
                        pygame.draw.rect(screen, (255, 0, 0), (hx - 10, hy + 6, 20, 6))
                        pygame.draw.rect(screen, (255, 0, 0), (hx - 6, hy + 12, 12, 6))

    pygame.display.flip()

pygame.quit()
sys.exit()