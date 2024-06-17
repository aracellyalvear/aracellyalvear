numeros=[
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0]
        ]

for fila in numeros :
    for columna in fila :
        num = int(input("Ingrese nro: >"))
        numeros[fila][columna] = num
        
print(numeros)

