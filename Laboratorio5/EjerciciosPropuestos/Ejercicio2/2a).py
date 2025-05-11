#Toda esta seccion es para poder usar los modulos fuera de esta carpeta
import sys
import os
# Agrega la carpeta padre de Ejercicio2 al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#.....

from chessPictures import knight
from interpreter import draw


knight_black = knight.negative()
figura = knight.join(knight_black)
figuraInvertida = figura.negative()
draw(figura.up(figuraInvertida))