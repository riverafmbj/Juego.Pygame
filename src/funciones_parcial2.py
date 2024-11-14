from sys import *
import pygame
from random import randint, randrange
from settings_parcial2 import *
from colisiones import punto_en_rectangulo
from images_and_sounds import *

def new_block(imagen = None, pos_x = 0, pos_y = 0, width = 50, height = 50, color = (255,255,255), borde = 0, radio = -1, speed_x = 5, speed_y = 10)->dict:
  if imagen:
    imagen = pygame.transform.scale(imagen, (width, height))
  return {"rect": pygame.Rect(pos_x, pos_y, width, height),
           "color": color,
           "borde": borde,
           "radio": radio,
           "img": imagen,
           "speed_x": speed_x,
           "speed_y": speed_y}

def new_celljr(imagen = None):
  celljr_width = 35
  celljr_height = 35
  return new_block(imagen, randint(WIDTH-celljr_width, (WIDTH*2)), randint(0, HEIGHT-celljr_height), celljr_width, celljr_height, YELLOW, 0, celljr_height//2, speed_x=randint(min_celljr_speed, max_celljr_speed))

def new_life(imagen = None):
  bean_width = 10
  bean_height = 10
  return new_block(imagen, randint(WIDTH-bean_width, (WIDTH*2)), randint(0, HEIGHT-bean_height), bean_width, bean_height, YELLOW, 0, bean_height//2, speed_x=randint(min_celljr_speed, max_celljr_speed))

def crear_blast(posicion: tuple[int, int], color:tuple[int, int, int]=RED, speed:int = 15, imagen = None):
  r = pygame.Rect(0, 0, laser_width, laser_height)
  r.midbottom = posicion
  return {"rect":r, 
          "color": color,
          "speed": speed,
          "img": imagen,
          "desviado": False}
# def crear_life(posicion: tuple[int, int], imagen)

def load_celljr_list(lista:list, cantidad, imagen = None, imagen2 = None):
  for i in range(cantidad//2):
    lista.append(new_celljr(imagen))
    lista.append(new_celljr(imagen2))

def load_life_list(lista:list, cantidad, imagen = None):
  for i in range(cantidad):
    lista.append(new_life(imagen))

def mostrar_texto(superficie: pygame.surface, texto: str, fuente: pygame.font.Font, posicion: tuple[int, int], color: tuple[int, int, int], color_fondo: tuple[int, int, int] = None):
   sup_texto = fuente.render(texto, True, color, color_fondo)
   rect_texto = sup_texto.get_rect(center = posicion)#le puedo pasar la posicion de movida
   superficie.blit(sup_texto, rect_texto)
   

def wait_user(tecla: int):
   continuar = True
   while continuar:
      for event in pygame.event.get():
      
        if event.type == pygame.QUIT:
         salir_juego()
      
        if event.type == pygame.KEYDOWN:#esto es si apreto la tecla
          if event.key == tecla:
            continuar = False

def wait_user_click(button_rect: pygame.Rect):
  continuar = True
  while continuar:
      for event in pygame.event.get():
      
        if event.type == pygame.QUIT:
         salir_juego()
      
        if event.type == pygame.MOUSEBUTTONDOWN:#esto es si apreto la tecla
          if event.button == 1:
            if punto_en_rectangulo(event.pos, button_rect):
              continuar = False

def mostrar_instrucciones(screen):
  fuente = pygame.font.Font("SEGUNDO PARCIAL/src/assets/font/saiyan_sans.ttf", 25)
  mostrar_texto(screen, "Protege a los guerreros Z de los Cell Jr.", fuente, (400,30), RED)
  mostrar_texto(screen, "Deberás enfrentarte a varias hordas de Cell Jr.", fuente, (400,60), RED)
  mostrar_texto(screen, "Usa tus rafagas de ki y tus patadas para eliminarlos.", fuente, (400,90), RED)
  mostrar_texto(screen, "Pulsa W para moverte hacia arriba y S para moverte hacia abajo.", fuente, (400,120), RED)
  mostrar_texto(screen, "Pulsa el click izquierdo del mouse para lanzar rafagas de ki.", fuente, (400,150), RED)
  mostrar_texto(screen, "Pulsa D para lanzar una patada cuando se acerquen.", fuente, (400,180), RED)
  mostrar_texto(screen, "Puedes usar la patada para devolverles sus rafagas de ki.", fuente, (400,210), RED)
  mostrar_texto(screen, "Si te pasan o sus rafagas de ki lo hacen, los guerreros Z perderan una vida.", fuente, (400,240), RED)
  mostrar_texto(screen, "Si pierden las cinco vidas, pierdes.", fuente, (400,270), RED)
  mostrar_texto(screen, "Intenta capturar las semillas voladoras para ganar vidas.", fuente, (400,300), RED)
  mostrar_texto(screen, "Buena suerte.", fuente, (400,330), RED)

def salir_juego():
   pygame.quit()
   exit()