#Toda esta seccion es para poder usar los modulos fuera de esta carpeta
import sys
import os
# Agrega la carpeta padre de Ejercicio2 al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#.....

from chessPictures import knight
from interpreter import draw

# Caballo blanco y su negativo (caballo negro)
knight_black = knight.negative()
# Parte superior: blanco | negro
fila_superior = knight.join(knight_black)
# Parte inferior: negro | blanco
fila_inferior = knight.join(knight_black).verticalMirror()
# Unimos ambas
resultado = fila_inferior.up(fila_superior)
# Dibujamos
draw(resultado)

