import sys
import os

# Agrega la carpeta padre de Ejercicio2 al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from chessPictures import rock
from interpreter import draw

# unir dos torres
figura = rock.join(rock)
draw(figura)