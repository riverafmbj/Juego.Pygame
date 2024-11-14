import pygame
from random import *

#screen
WIDTH = 800#se deben pasar como variables y no como numeros
HEIGHT = 600
MID_WIDTH_SCREEN = WIDTH // 2
MID_HEIGHT_SCREEN = HEIGHT // 2
SCREEN_SIZE = (WIDTH, HEIGHT)
SCREEN_CENTER = (MID_WIDTH_SCREEN, MID_HEIGHT_SCREEN)
ORIGIN = (0, 0)

#title
TITLE_POS = (MID_WIDTH_SCREEN, 150)

#scores
SCORE_POS = (MID_WIDTH_SCREEN, 50)
LAST_SCORE_POS = (150, 50)
MAX_SCORE_POS = (WIDTH - 150, 50)

#menu
MUTE_POS = (60, HEIGHT-50)
MESSAGE_START_POS = (MID_WIDTH_SCREEN, HEIGHT-50)
START_BUTTON_SIZE = (300, 300)
START_BUTTON_POS = (SCREEN_CENTER)

#lifes
life_initial_pos_x = 75
life_pos_y = 40
LIFE_POS = (life_initial_pos_x, life_pos_y)
life_speed = 5

FPS = 30

#colors - RGB system
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CUSTOM = (226, 203, 95)

#block
y = 50
x = 50
block_width = 50
block_height = 50
BORDE = 0
BLOCK_SIZE = x, y, block_width, block_height

#laser
laser_width = 16
laser_height = 6

#configuro los movimientos
move_left = False
move_right = False
move_up = False
move_down = False

min_celljr_speed = 2
max_celljr_speed = 5

