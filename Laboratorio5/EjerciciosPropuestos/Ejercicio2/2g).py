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
