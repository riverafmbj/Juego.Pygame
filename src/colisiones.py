
def detectar_colision(rect_1, rect_2)->bool:
  if punto_en_rectangulo(rect_1.topleft, rect_2) or \
    punto_en_rectangulo(rect_1.topright, rect_2) or \
    punto_en_rectangulo(rect_1.bottomleft, rect_2) or \
    punto_en_rectangulo(rect_1.bottomright, rect_2) or \
    punto_en_rectangulo(rect_2.topleft, rect_1) or \
    punto_en_rectangulo(rect_2.topright, rect_1) or \
    punto_en_rectangulo(rect_2.bottomleft, rect_1) or \
    punto_en_rectangulo(rect_2.bottomright, rect_1):
      return True
  else:
      return False

def punto_en_rectangulo(punto, rect)->bool:
  x, y = punto
  if x >= rect.left and x <= rect.right and y >= rect.top and y <= rect.bottom:
    return True
  else:
    return False

def distancia_entre_puntos(punto1: tuple[int, int], punto2: tuple[int, int])->float:
   cateto_adyacente = punto1[0] - punto2[0]
   cateto_opuesto = punto1[1] - punto2[1]
   distancia = (cateto_adyacente**2 + cateto_opuesto**2) ** 0.5#el ** 0.5 saca la raiz cuadrada
   return distancia

def colision_circulos(rect1, rect2)->bool:
   r1 = rect1.width // 2
   r2 = rect2.height // 2
   distancia = distancia_entre_puntos(rect1.center, rect2.center)

   if distancia <= r1 + r2:
      return True
   else:
      return False




