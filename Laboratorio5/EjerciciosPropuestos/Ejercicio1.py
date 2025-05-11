from picture import Picture
img = [
    "abc",
    "def",
    "ghi"
]

pic = Picture(img)
def mostrar(picture):
    for fila in picture.img:
        print(fila)
    print()  # línea en blanco para separar

print("Original:")
mostrar(pic)

print("Espejo vertical:")
mostrar(pic.verticalMirror())

print("Espejo horizontal:")
mostrar(pic.horizontalMirror())

print("Negative:")
# Este metodo se probara en el ejercicio 2
mostrar(pic.negative())

print("Unirse con uno mismmo/ Join with itself:")
mostrar(pic.join(pic))

print("Arriba con uno mismo /Up with itself:")
mostrar(pic.up(pic))

print("Debajo (con anulación de espacio) / Under (with space override):")
# una figura con espacio para ver el efecto
mask = Picture([
    " A ",
    "   ",
    " C "
])
mostrar(pic.under(mask))

print("Horizontal Repeat (x2):")
mostrar(pic.horizontalRepeat(4))

print("Vertical Repeat (x2):")
mostrar(pic.verticalRepeat(4))

print("Rotate 90° clockwise:")
mostrar(pic.rotate())