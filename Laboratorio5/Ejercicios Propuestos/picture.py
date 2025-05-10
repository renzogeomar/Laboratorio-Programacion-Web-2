from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    nueva_img = []
    for fila in self.img:
      nueva_img.append(fila[::-1])  # invierte cada línea
    return Picture(nueva_img)

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    nueva_img = []
    for i in range(len(self.img) - 1, -1, -1):
      nueva_img.append(self.img[i])
    return Picture(nueva_img)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    nueva_img = []
    for fila in self.img:
      nueva_fila = ''
      for caracter in fila:
        nuevo = self._invColor(caracter)
        nueva_fila += nuevo
      nueva_img.append(nueva_fila)
    return Picture(nueva_img)

  def join(self, p):
    """ Une la figura actual con otra al lado derecho """
    nueva_img = []
    for i in range(len(self.img)):
      nueva_linea = self.img[i] + p.img[i]
      nueva_img.append(nueva_linea)
    return Picture(nueva_img)

  def up(self, p):
    """ Pone la imagen p encima de la actual """
    return Picture(p.img + self.img)

  def under(self, p):
    """ Pone la imagen p encima de esta, sobrescribiendo los caracteres no vacíos """
    nueva_img = []
    for i in range(len(self.img)):
      linea1 = self.img[i]
      linea2 = p.img[i]
      nueva_linea = ''
      for j in range(len(linea1)):
        if linea2[j] != ' ':
          nueva_linea += linea2[j]
        else:
          nueva_linea += linea1[j]
      nueva_img.append(nueva_linea)
    return Picture(nueva_img)
  
  def horizontalRepeat(self, n):
    """ Repite la imagen horizontalmente n veces """
    nueva_img = []
    for fila in self.img:
      nueva_img.append(fila * n)
    return Picture(nueva_img)

  def verticalRepeat(self, n):
    """ Repite la imagen verticalmente n veces """
    nueva_img = []
    for _ in range(n):
      for fila in self.img:
        nueva_img.append(fila)
    return Picture(nueva_img)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)