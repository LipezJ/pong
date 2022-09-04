import random as rn
import os

def imprimir_tablero():
    os.system('cls')
    for tablero_ in tablero:
        print(tablero_)
    os.system('sleep 0.5')
def buscar_uno():
    for i in range(len(tablero)):
        if 1 in tablero[i]:
            return [i, tablero[i].index(1)]
def posibilidades_():
    if (actual[0] == 0 and actual[1] == 0) or (actual[0] == 0 and actual[1] == len(tablero[0])-1) or (actual[0] == len(tablero)-1 and actual[1] == 0) or (actual[0] == len(tablero)-1 and actual[1] == len(tablero[0])-1):
        return [4]
    if actual[0] == len(tablero)-1:
        posibilidades_ = [0, 1]
    elif actual[0] == 0:
        posibilidades_ = [2, 3]
    elif actual[1] == len(tablero[0])-1:
        posibilidades_ = [0, 3]
    elif actual[1] == 0:
        posibilidades_ = [1, 2]
    else:
        posibilidades_ = [0,1,2,3]
    return posibilidades_

tablero = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
movimientos = {
    0: [-1, -1], 1: [-1, 1], 
    2: [1, 1], 3: [1, -1]
}
movimientos_ = {
    '-1-1': 0, '-11': 1,
    '1-1': 3, '11': 2,
    '00': 4
}
movimientos__ = {0: 2, 1: 3, 2: 0, 3: 1}

punto = 1

inicio_fila = rn.randint(0, len(tablero)-1)
inicio_columna = rn.randint(0, len(tablero[0])-1)

tablero[inicio_fila][inicio_columna] = 1
actual = [inicio_fila, inicio_columna]

imprimir_tablero()
for i in range(30):

    anterior = actual
    actual = buscar_uno()
    
    #calcular el tipo de movimiento anterior
    tipo = str(actual[0] - anterior[0]) + str(actual[1] - anterior[1])
    tipo = movimientos_[tipo]

    #ejecutar la funcion para saber cuantas posibilidades hay en el movimiento
    posibilidades = posibilidades_()
    
    #primer movimiento
    if actual == anterior:
        posibilidades = rn.choice(posibilidades_())
        nuevo = movimientos[posibilidades]
        nuevo = [actual[0] + nuevo[0], actual[1] + nuevo[1]]
    
    #esquinas
    elif posibilidades[0] == 4:
        nuevo = anterior

    #movimientto normal
    elif len(posibilidades) == 4:
        nuevo = [actual[0] - anterior[0], actual[1] - anterior[1]]
        nuevo = [actual[0] + nuevo[0], actual[1] + nuevo[1]]
    
    #rebotes
    else:
        tipo_ = movimientos__[tipo]
        posibilidades.remove(tipo_)
        nuevo = movimientos[posibilidades[0]]
        nuevo = [actual[0] + nuevo[0], actual[1] + nuevo[1]]

    tablero[nuevo[0]][nuevo[1]] = punto
    tablero[actual[0]][actual[1]] = 0
    imprimir_tablero()