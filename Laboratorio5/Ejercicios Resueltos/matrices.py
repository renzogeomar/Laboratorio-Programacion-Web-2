def esEscalar(m):
    d = m[0][0]
    for i in range(len(m)):
        for j in range(len(m)):
            if i != j:
                if m[i][j] != 0:
                    print(m[i][j])
                    return False
            elif m[i][j] != d:
                print(m[i][j])
                return False
    return True

def esUnitaria(m):
    return m[0][0] == 1 and esEscalar(m)

# MATRICES DE PRUEBA
m1 = [
    [5, 0, 0],
    [0, 5, 0],
    [0, 0, 5]
]

m2 = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

m3 = [
    [1, 2, 3],
    [0, 1, 0],
    [0, 0, 1]
]

# PRUEBAS
print("¿m1 es escalar?", esEscalar(m1))     # True
print("¿m2 es unitaria?", esUnitaria(m2))   # True
print("¿m3 es escalar?", esEscalar(m3))     # False
print("¿m3 es unitaria?", esUnitaria(m3))   # False