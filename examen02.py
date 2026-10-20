laberinto = [
    ['F', 0, 4, 3, 1, 1, 3, 4, 1],
    [3,   0, 1, 0, 0, 1, 0, 1, 3],
    [4,   1, 3, 1, 4, 3, 1, 4, 1],
    [1,   0, 0, 0, 1, 0, 0, 0, 1],
    [3,   4, 1, 3, 4, 1, 3, 4, 1],
    [1,   0, 1, 0, 0, 0, 1, 0, 1],
    [4,   3, 4, 1, 3, 4, 1, 3, 4],
    [1,   0, 0, 1, 0, 0, 1, 0, 1],
    ['I', 3, 4, 1, 1, 3, 4, 1, 1]
]

camino = [row[:] for row in laberinto]
visitados = [[False for _ in range(9)] for _ in range(9)]

encontrado = False
puntos_totales = 0

def resolver(x, y, puntos):
    global encontrado, puntos_totales
    
    if x < 0 or x > 8 or y < 0 or y > 8:
        return
    if laberinto[x][y] == 0 or visitados[x][y]:
        return

    val = laberinto[x][y]
    if val == 'I' or val == 'F':
        puntos_actuales = puntos + 1
    else:
        puntos_actuales = puntos + int(val)

    visitados[x][y] = True
    camino[x][y] = '*'

    if x == 0 and y == 0:
        if puntos_actuales >= 23:
            puntos_totales = puntos_actuales
            encontrado = True
        visitados[x][y] = False
        if not encontrado:
            camino[x][y] = 'F'
        return

    movimientos = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    for dx, dy in movimientos:
        if not encontrado:
            resolver(x + dx, y + dy, puntos_actuales)

    if not encontrado:
        visitados[x][y] = False
        if laberinto[x][y] == 'I':
            camino[x][y] = 'I'
        elif laberinto[x][y] == 'F':
            camino[x][y] = 'F'
        else:
            camino[x][y] = laberinto[x][y]

print("=== LABERINTO ORIGINAL ===")
for fila in laberinto:
    print(" ".join(str(c) for c in fila))
print()

resolver(8, 0, 0)

if encontrado:
    print(f"¡SALIDA ENCONTRADA! Puntos obtenidos: {puntos_totales}")
    print("=== MATRIZ CON EL CAMINO (*) ===")
    for fila in camino:
        print(" ".join(str(c) for c in fila))
else:
    print("No se encontró un camino con 23 o más puntos.")