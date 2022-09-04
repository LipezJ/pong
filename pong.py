#librerias
from pytimedinput import timedKey
import random as rn
import os
import time

#variables
#   generales
tablero = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
area = [0, 0, 0, 0, 0, 0, 0, '|', '|', 0, 0, 0, 0, 0, 0]
#   tablero
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
#   area
movimientos_area = {'w': -1, 'd': 1}


#funciones generales
#   imprimir
def imprimir():
    os.system('cls')
    for i in range(len(area)):
        print(area[i], tablero[i])

#funciones para el tablero
#   buscar la "pelota"
def buscar_uno():
    for i in range(len(tablero)):
        if 1 in tablero[i]:
            return [i, tablero[i].index(1)]
#   calcular las posibilidades
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

#funciones para el area de raqueta
#   movimientos
def mover():
    nuevo_area = [
        actual_area[0] + movimientos_area[key], 
        actual_area[1] + movimientos_area[key]
    ]
    area[actual_area[0]] = 0
    area[actual_area[1]] = 0  
    area[nuevo_area[0]] = '|'
    area[nuevo_area[1]] = '|'

# codigo

#inicializando variables
inicio_fila = rn.randint(0, len(tablero)-1)
inicio_columna = rn.randint(0, len(tablero[0])-1)

tablero[inicio_fila][inicio_columna] = 1
actual = [inicio_fila, inicio_columna]

#bucle general
while True:

    #calcular posicion de la raqueta
    actual_area = [area.index('|')]
    actual_area.append(actual_area[0]+1)
    #calcular posicion de la pelota
    anterior = actual   
    actual = buscar_uno()

    #calcular el tipo de movimiento anterior
    tipo = str(actual[0] - anterior[0]) + str(actual[1] - anterior[1])
    tipo = movimientos_[tipo]
    #ejecutar la funcion para saber cuantas posibilidades hay en el movimiento
    posibilidades = posibilidades_()

    #escucha de tevlas
    key, timeout = timedKey(allowCharacters='wdq', timeout=0.2)

    #   area
    #si se presiona 'q' se saldra del programa
    if key == 'q':
        print(exit())

    #si se presiona una tecla procede a evaluar el movimiento
    if not timeout:
        #movimiento hacia arriba
        if key == 'w' and actual_area[0] > 0:
            mover()
        #movimiento hacia abajo
        elif key == 'd' and actual_area[1] < len(area)-1:
            mover()
        time.sleep(0.1)
    
    #   tablero
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

    tablero[nuevo[0]][nuevo[1]] = 1
    tablero[actual[0]][actual[1]] = 0
    imprimir()