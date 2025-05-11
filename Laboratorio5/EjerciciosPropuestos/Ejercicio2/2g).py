#Toda esta seccion es para poder usar los modulos fuera de esta carpeta
import sys
import os
# Agrega la carpeta padre de Ejercicio2 al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#..... 

from chessPictures import square
from chessPictures import bishop
from chessPictures import king
from chessPictures import knight
from chessPictures import pawn
from chessPictures import square
from chessPictures import queen
from chessPictures import rock
from interpreter import draw

# Parte del tablero sin piezas
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
tableroSinPiezas = fila2.up(fila1).up(fila2).up(fila1)
#------------------------------------------------------------

# Parte del tablero con piezas
parteConPiezas = fila1.up(fila2)
draw(parteConPiezas)
