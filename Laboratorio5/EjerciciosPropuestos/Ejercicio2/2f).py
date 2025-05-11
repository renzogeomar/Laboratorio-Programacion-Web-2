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
fila1 = black_square
for i in range(3):  # ya hay 1, agregamos 3 pares más
    fila1 = fila1.join(square).join(black_square)
# Falta una casilla negra al final para tener 8
fila1 = fila1.join(square)

# Alternar: iniciando con blanco
fila2 = square
for i in range(3):  # ya hay 1, agregamos 3 pares más
    fila2 = fila2.join(black_square).join(square)
# Falta una casilla negra al final para tener 8
fila2 = fila2.join(black_square)
tablero = fila2.up(fila1).up(fila2).up(fila1)

draw(tablero)