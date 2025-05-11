#Toda esta seccion es para poder usar los modulos fuera de esta carpeta
import sys
import os
# Agrega la carpeta padre de Ejercicio2 al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#..... 

from chessPictures import square
from interpreter import draw

black_square = square.negative()

# Alternar: iniciando con negro
fila = black_square
for i in range(3):  # ya hay 1, agregamos 3 pares más
    fila = fila.join(square).join(black_square)
# Falta una casilla negra al final para tener 8
fila = fila.join(square)
draw(fila)