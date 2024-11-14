import pygame #1)importamos la bibliotecta
from random import *
from settings_parcial2 import *
from colisiones import *
from sys import exit
from funciones_parcial2 import *
from images_and_sounds import *


#2)inizializamos los módulos
pygame.init()

#3)configuracion

clock = pygame.time.Clock()
SCREEN = pygame.display.set_mode(SCREEN_SIZE)

pygame.display.set_caption("Dragon Ball Z - Gohan's Revenge")


#cargo musica
pygame.mixer.music.load("SEGUNDO PARCIAL/src/assets/music/intro_music.mp3")#musica de fond. no se guarda en una variable como los sonidos


#cargo fuente

fuente = pygame.font.Font("SEGUNDO PARCIAL/src/assets/font/saiyan_sans.ttf", 50)

pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.6)




imagen_evil_ki_blast_path = "SEGUNDO PARCIAL/src/assets/images/evil_ki_blast.png"

def main_menu():
    while True:
        blitear_fondo(background_menu)
        mouse_over_button = False
        
        
  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir_juego()

        if draw_button("COMENZAR", pygame.Rect(500, 200, 210, 50), YELLOW, RED, comenzar_juego):
            mouse_over_button = True
        if draw_button("INSTRUCCIONES", pygame.Rect(500, 300, 290, 50), YELLOW, RED, go_to_screen2):
            mouse_over_button = True
        if draw_button("OPCIONES", pygame.Rect(500, 400, 200, 50), YELLOW, RED, go_to_screen3):
            mouse_over_button = True
        if draw_button("SALIR", pygame.Rect(500, 500, 200, 50), RED, YELLOW, salir_juego):
            mouse_over_button = True

        if mouse_over_button:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        pygame.display.flip()

def comenzar_juego():
  # bucle principal
  is_running = True
  while True:
    #creamos el bloques
    #evento personalizado
    TIMERCOIN = pygame.USEREVENT + 1 
    CHANGE_IMAGE_EVENT = pygame.USEREVENT + 2
    pygame.time.set_timer(CHANGE_IMAGE_EVENT, 5000)
    explosion_time = 0

      
    block = new_block(imagen_gohan, 50, HEIGHT//2, x, y, 0, 30)
    
    z_warriors_lifes = []
    count_lifes = 5
    separacion_vidas = 20
    

    count_cell_jrs = 10
    cell_jrs = []
    load_celljr_list(cell_jrs, count_cell_jrs, imagen_celljr, imagen_celljr_2)
    explosion_position = None
    evil_blasts = []
    

    pygame.mixer.music.load("SEGUNDO PARCIAL/src/assets/music/battle_music.mp3")
    pygame.mixer.music.play(-1)#le podemos pasar 1)si entra en loop (-1 para q se repita eternamente) 2)start: un valor entero que indica en que segundo empieza 3)fade: un valor entero q indica que vaya creciendo en sonido y que no arranque de golpe
    pygame.mixer.music.set_volume(0.1)#seteamos el volumen
    #se deberian guardar los scores en json o csv y los valores de musica en settings
    playing_music = True

    pygame.time.set_timer(TIMERCOIN, 5000)#le podemos pasar 1)el evento. 2) cada cuanto tiempo ocurre el evento(en milisegundos). 3)el loop.

    score = 0
    max_score = 0
    move_up = False
    move_down = False
    attack = False
    blasts = []

  # juego principal
    
    
    while is_running:
      
      pygame.mouse.set_visible(False)
      clock.tick(FPS)
      #se encarga de ponerle un delay al while
      # print(contador)
    #4)relevar los eventos: preguntar que eventos están ocurriendo
      for event in pygame.event.get():
      #el get devuelve una lista de eventos, la voy a poder correr con un for
      #5)Analizar los eventos:
        #evento: el usuario sale del juego
        if event.type == pygame.QUIT:
          salir_juego()
        
        #evento: se presionó una tecla
        if event.type == pygame.KEYDOWN:#esto es si apreto la tecla
          
          if event.key == pygame.K_w:
            move_up = True
            move_down = False
            block["img"] = imagen_gohan_move_up
          
          if event.key == pygame.K_s: #esto es la tecla flecha para abajo
            move_down = True
            block["img"] = imagen_gohan_move_down
            move_up = False
          
          if event.key == pygame.K_d:
            attack = True
            block["img"] = imagen_gohan_kick
            

          if event.key == pygame.K_m:
              if playing_music:
                pygame.mixer.music.pause()
              else:
                pygame.mixer.music.unpause()
              playing_music = not playing_music
          #si presiono p se pausa el juego
          if event.key == pygame.K_p:
              pygame.mixer.music.pause()
              mostrar_texto(SCREEN, "PAUSA", fuente, SCREEN_CENTER, MAGENTA)
              pygame.display.flip()
              wait_user(pygame.K_p)
              
              if playing_music:
                pygame.mixer.music.unpause()
                        

        #evento: se liberó la tecla
        if event.type == pygame.KEYUP:#esto es si suelto la tecla
          #Cambia la imagen de cuando está subiendo a la normal
          if event.key == pygame.K_w:
            block["img"] = imagen_gohan
            move_up = False
          #Cambia la imagen de cuando está bajando a la normal
          if event.key == pygame.K_s: #esto es la tecla flecha para abajo
            block["img"] = imagen_gohan
            move_down = False
          #Cambia la imagen de la patada a la normal
          if event.key == pygame.K_d:
            attack = False
            block["img"] = imagen_gohan
        #Gohan dispara
        if event.type == pygame.MOUSEBUTTONDOWN:#1)boton izq 2)boton medio 3)boton der 4)scroll down 5)scroll up
          if event.button == 1:
            block["img"] = imagen_ki_shot
            blast = crear_blast(block["rect"].midright, imagen=imagen_ki_blast)  
            ki_blast_sound.play()
            blasts.append(blast)
        #Cambia la imagen a Gohan cuando deja de disparar   
        if event.type == pygame.MOUSEBUTTONUP:
          if event.button == 1 and move_down == False and move_up == False:
            block["img"] = imagen_gohan

        #evento personalizado
        #EVENTO: HACE QUE UN CELL JR. RANDOM DISPARE UNA RAFAGA
        if event.type == CHANGE_IMAGE_EVENT:
          selected_celljr = cell_jrs[randint(0, len(cell_jrs) - 1)]
          selected_celljr["img"] = imagen_celljr_ki_shot
          selected_celljr["shot_time"] = pygame.time.get_ticks()
          evil_blast = crear_blast(selected_celljr["rect"].midleft, pygame.transform.flip(pygame.image.load("SEGUNDO PARCIAL/src/assets/images/evil_ki_blast.png"), True,False))
          ki_blast_sound.play()
          evil_blasts.append(evil_blast)
        
        # if event.type == TIMERCOIN:
        #   special_coin = new_coin(imagen_asteroide)
        #   cell_jrs.append(special_coin)
        
        # if event.type == GAME_TIME_OUT:
        #   is_running = False
      
    
      
      if move_up and block["rect"].top > 0:
          block["rect"].top -= block["speed_y"]
          if block["rect"].top == 0:
            block["img"] = imagen_gohan

      if move_down and block["rect"].bottom < HEIGHT:
          block["rect"].bottom += block["speed_y"]
          if block["rect"].bottom == HEIGHT:
            block["img"] = imagen_gohan

      pygame.mouse.set_pos(block["rect"].center)

      for blast in blasts:
        blast["rect"].move_ip(blast["speed"], 0)
        
      for evil_blast in evil_blasts[:]:
        if evil_blast["desviado"] == False:
            evil_blast["rect"].move_ip(-7, 0)
            imagen_evil_ki_blast = pygame.transform.flip(pygame.image.load("SEGUNDO PARCIAL/src/assets/images/evil_ki_blast.png"), True,False)
        else:
            evil_blast["rect"].move_ip(12, 0)
        
        if evil_blast["rect"].right < 0:
            z_warriors_lifes.pop()
            evil_blasts.remove(evil_blast)
        
        if z_warriors_lifes == []:
            is_running = False

      for celljr in cell_jrs:
        celljr["rect"].move_ip(-celljr["speed_x"],0)#1)cuanto se tiene q mover en x 2)cuanto se tiene q mover en y
        if celljr["rect"].right < 0:
          celljr["rect"].left = WIDTH
          z_warriors_lifes.pop()
          
          if z_warriors_lifes == []:
            is_running = False

      for celljr in cell_jrs:
        if "shot_time" in celljr:
            elapsed_time = pygame.time.get_ticks() - celljr["shot_time"]
            if elapsed_time > 700:
                celljr["img"] = imagen_celljr
                del celljr["shot_time"]

  # COLISION ENTRE BLASTS
      for blast in blasts[:]: #shallow copy de las listas para que no haya problemas de iteracion
        for evil_blast in evil_blasts[:]:
          if colision_circulos(blast["rect"], evil_blast["rect"]):
            explosion_sound.play()
            blasts.remove(blast)   
            explosion_time = pygame.time.get_ticks()
            explosion_position = evil_blast["rect"].center
            evil_blasts.remove(evil_blast)
          
          
    
    # COLISION GOHAN Y CELL JRS.  
      for celljr in cell_jrs[:]:
        if attack == True and colision_circulos(block["rect"], celljr["rect"]):
            cell_jrs.remove(celljr)
            explosion_sound.play()
            score += 1
      
        for evil_blast in evil_blasts[:]:
          if block["img"] == imagen_gohan_kick and colision_circulos(block["rect"], evil_blast["rect"]):
              evil_blast["desviado"] = True
              imagen_evil_ki_blast = pygame.image.load("SEGUNDO PARCIAL/src/assets/images/evil_ki_blast.png")
              # evil_blast["rect"].height = 70 

    # COLISION ENTRE BLAST Y CELL JRS.
        for blast in blasts:
          if colision_circulos(blast["rect"], celljr["rect"]):
            explosion_sound.play()
            score += 1
            blasts.remove(blast)       
            explosion_time = pygame.time.get_ticks()
            explosion_position = celljr["rect"].center
            cell_jrs.remove(celljr) 
      
      for celljr in cell_jrs[:]:
          for evil_blast in evil_blasts[:]:
              if evil_blast["desviado"] == True and colision_circulos(evil_blast["rect"], celljr["rect"]):
                  explosion_sound.play()
                  score += 3
                  evil_blasts.remove(evil_blast)
                  explosion_time = pygame.time.get_ticks()
                  explosion_position = celljr["rect"].center
                  cell_jrs.remove(celljr)


      if cell_jrs == []:
        load_celljr_list(cell_jrs, count_cell_jrs, imagen_celljr, imagen_celljr_2)
      
      if z_warriors_lifes == []:
        load_life_list(z_warriors_lifes, count_lifes, imagen_life)    


      #dibujar la pantalla
      SCREEN.blit(background_arena, ORIGIN)
      
      SCREEN.blit(block["img"], block["rect"])

      i_life_list_pos = 0
      for life in z_warriors_lifes:
          position_x = life_initial_pos_x + i_life_list_pos * separacion_vidas
          SCREEN.blit(imagen_life, (position_x, life_pos_y))
          i_life_list_pos += 1
      

      for blast in blasts:
          SCREEN.blit(blast["img"], blast["rect"])

      for celljr in cell_jrs:
          SCREEN.blit(celljr["img"], celljr["rect"])

      for evil_blast in evil_blasts:
        SCREEN.blit(imagen_evil_ki_blast, evil_blast["rect"])

      if explosion_time > 0:
              elapsed_time = pygame.time.get_ticks() - explosion_time
              if elapsed_time < 500:
                SCREEN.blit(imagen_explosion, imagen_explosion.get_rect(center=explosion_position))
              else:
                explosion_time = 0
                explosion_position = None
      
      
      mostrar_texto(SCREEN, F"Score: {score}", fuente, SCORE_POS, BLUE)
      
      
      if playing_music == False:
        mostrar_texto(SCREEN, "Mute", fuente, MUTE_POS, GREEN)
      
      #7)Actualizar la pantalla
      pygame.display.flip()

    
      #pantalla Game Over
    if score > max_score:
      max_score = score
      #game_over_sound.play()
    pygame.mixer.music.stop()
    SCREEN.blit(background_game_over, ORIGIN)
    mostrar_texto(SCREEN, F"Last Score: {score}", fuente, LAST_SCORE_POS, CYAN)
    mostrar_texto(SCREEN, F"Max Score: {max_score}", fuente, MAX_SCORE_POS, CYAN)
    mostrar_texto(SCREEN, "GAME OVER", fuente, SCREEN_CENTER, BLUE)
    mostrar_texto(SCREEN, "Pulsa SPACE para comenzar", fuente, MESSAGE_START_POS, RED)
    wait_user(pygame.K_SPACE)
    

def screen2():
    while True:
        blitear_fondo(background_arena)
        mouse_over_button = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir_juego()

        mostrar_instrucciones(SCREEN)

        if draw_button("Volver", pygame.Rect(300, 500, 200, 50), GREEN, YELLOW, main_menu):
            mouse_over_button = True

        if mouse_over_button:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        pygame.display.flip()

def screen3():
    while True:
        blitear_fondo(background_menu)
        mouse_over_button = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir_juego()

        text_surf = fuente.render("Screen 3", True, BLACK)
        SCREEN.blit(text_surf, (WIDTH // 2 - text_surf.get_width() // 2, HEIGHT // 2 - text_surf.get_height() // 2))

        if draw_button("Volver", pygame.Rect(300, 500, 200, 50), GREEN, YELLOW, main_menu):
            mouse_over_button = True

        if mouse_over_button:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        pygame.display.flip()

def go_to_screen2():
    screen2()

def go_to_screen3():
    screen3()

def blitear_fondo(imagen):
   SCREEN.blit(imagen, ORIGIN)
   

def draw_button(text, rect, color, hover_color, action=None):
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    hovered = rect.collidepoint(mouse_pos)
    
    if hovered:
        pygame.draw.rect(SCREEN, hover_color, rect)
        if click[0] == 1 and action: #el 1 es como decirle True
            pygame.time.delay(200)
            action()
    else:
        pygame.draw.rect(SCREEN, color, rect)
    
    text_surf = fuente.render(text, True, BLACK)
    SCREEN.blit(text_surf, (rect.x + (rect.width - text_surf.get_width()) // 2, rect.y + (rect.height - text_surf.get_height()) // 2))
    
    return hovered


main_menu()
salir_juego()
