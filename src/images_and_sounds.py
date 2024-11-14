import pygame
from settings_parcial2 import *

pygame.init()

# IMÁGENES
# backgrounds
background_menu = pygame.transform.scale(
  pygame.image.load("SEGUNDO PARCIAL/src/assets/images/background_menu2.jpg"), (SCREEN_SIZE))
background_arena = pygame.transform.scale(
   pygame.image.load("SEGUNDO PARCIAL/src/assets/images/background_arena.png"), (SCREEN_SIZE))
background_game_over =pygame.transform.scale(
  pygame.image.load("SEGUNDO PARCIAL/src/assets/images/background_game_over.jpg"), (SCREEN_SIZE))

# personajes
imagen_gohan = pygame.image.load("SEGUNDO PARCIAL/src/assets/images/gohan_standard_pose.png")
imagen_celljr = pygame.transform.flip(pygame.image.load("SEGUNDO PARCIAL/src/assets/images/celljr_flying_1.png"), True,False)
imagen_celljr_2 = pygame.transform.flip(pygame.image.load("SEGUNDO PARCIAL/src/assets/images/celljr_flying_2.png"), True,False)

#movimientos
imagen_ki_shot = pygame.image.load("SEGUNDO PARCIAL/src/assets/images/gohan_ki_shot.png")
imagen_celljr_ki_shot = pygame.transform.flip(pygame.image.load("SEGUNDO PARCIAL/src/assets/images/celljr_ki_shot.png"), True,False)
imagen_gohan_move_up = pygame.image.load("SEGUNDO PARCIAL/src/assets/images/gohan_up.png")
imagen_gohan_move_down = pygame.image.load("SEGUNDO PARCIAL/src/assets/images/gohan_down.png")
imagen_gohan_kick = pygame.transform.flip(pygame.image.load("SEGUNDO PARCIAL/src/assets/images/gohan_kick.png"), True,False)

# efectos
imagen_ki_blast = pygame.image.load("SEGUNDO PARCIAL/src/assets/images/ki_blast.png")
imagen_explosion = pygame.image.load("SEGUNDO PARCIAL/src/assets/images/explosion.png")
imagen_evil_ki_blast = pygame.transform.flip(pygame.image.load("SEGUNDO PARCIAL/src/assets/images/evil_ki_blast.png"), True,False)

#otros
imagen_life = pygame.transform.scale(pygame.image.load("SEGUNDO PARCIAL/src/assets/images/life.png"), (20,20))

# menu
start_button = pygame.transform.scale(
    pygame.image.load("SEGUNDO PARCIAL/src/assets/images/start_button.png"), START_BUTTON_SIZE)
rect_start_button = start_button.get_rect(center = START_BUTTON_POS)


# SONIDOS
explosion_sound = pygame.mixer.Sound("SEGUNDO PARCIAL/src/assets/sounds/explosion.mp3")
ki_blast_sound = pygame.mixer.Sound("SEGUNDO PARCIAL/src/assets/sounds/ki_blast.mp3")

