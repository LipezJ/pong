#librerias
from pytimedinput import timedKey
import random as rn
import os
import time

#variables
#   generales
tablero = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
area = [0, 0, 0, 0, 0, 0, 0, '|', '|', 0, 0, 0, 0, 0, 0]
area2 = [0, 0, 0, 0, 0, 0, 0, '|', '|', 0, 0, 0, 0, 0, 0]
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
movimientos_area = {'w': -1, 'd': 1, 'k': -1, 'm': 1}


#funciones generales
#   imprimir
def imprimir():
    os.system('cls')
    print()
    for i in range(len(tablero[0])+1):
        print('x', end='')
    print()
    for i in range(len(area)):
        if area[i] == '|':
            print(area[i], end='')
        else:
            print(' ', end='')

        for j in range(len(tablero[0])):
            if tablero[i][j] == 1:
                print('O', end='')
            elif j == centro:
                print('|', end='')
            else:
                print(' ', end='')
        if area2[i] == '|':
            print(area2[i], end='')
        else:
            print(' ', end='')
        print()
    for i in range(len(tablero[0])+1):
        print('x', end='')
    print()
    print('puntos 1: ', puntos, 'puntos 2: ', puntos2)
#   elegir una nueva caciila
def random_():
    tablero[actual[0]][actual[1]] = 0
    inicio_fila = rn.randint(0, len(tablero)-1)
    inicio_columna = (len(tablero[0])-1)//2

    tablero[inicio_fila][inicio_columna] = 1
    return [inicio_fila, inicio_columna]

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
def mover2():
    nuevo_area2 = [
        actual_area2[0] + movimientos_area[key], 
        actual_area2[1] + movimientos_area[key]
    ]
    area2[actual_area2[0]] = 0
    area2[actual_area2[1]] = 0  
    area2[nuevo_area2[0]] = '|'
    area2[nuevo_area2[1]] = '|'

# codigo

#inicializando variables
centro = (len(tablero[0])-1)//2
inicio_fila = rn.randint(0, len(tablero)-1)
inicio_columna = centro

tablero[inicio_fila][inicio_columna] = 1
actual = [inicio_fila, inicio_columna]

puntos = 0
puntos2 = 0

#bucle general
while True:

    #calcular posicion de la raqueta
    actual_area = [area.index('|')]
    actual_area.append(actual_area[0]+1)

    actual_area2 = [area2.index('|')]
    actual_area2.append(actual_area2[0]+1)
    #calcular posicion de la pelota
    anterior = actual   
    actual = buscar_uno()

    #calcular el tipo de movimiento anterior
    tipo = str(actual[0] - anterior[0]) + str(actual[1] - anterior[1])
    tipo = movimientos_[tipo]
    #ejecutar la funcion para saber cuantas posibilidades hay en el movimiento
    posibilidades = posibilidades_()

    #escucha de teclas
    key, timeout = timedKey(allowCharacters='wdqkm', timeout=0.1)

    #   area
    #si se presiona 'q' se saldra del programa
    if key == 'q':
        print(exit())
    elif puntos < -1:
        os.system('cls')
        print('Perdiste! jugador 1')
        time.sleep(1.5)
        print(exit())
    elif puntos2 < -1:
        os.system('cls')
        print('Perdiste! jugador 2')
        time.sleep(1.5)
        print(exit())
    elif puntos == 10:
        os.system('cls')
        print('Ganaste! jugador 1')
        time.sleep(1.5)
        print(exit())
    elif puntos2 == 10:
        os.system('cls')
        print('Ganaste! jugador 2')
        time.sleep(1.5)
        print(exit())

    #si se presiona una tecla procede a evaluar el movimiento
    if not timeout:
        #movimiento hacia arriba
        if key == 'w' and actual_area[0] > 0:
            mover()
        #movimiento hacia abajo
        elif key == 'd' and actual_area[1] < len(area)-1:
            mover()
        #movimiento hacia arriba2
        if key == 'k' and actual_area2[0] > 0:
            mover2()
        #movimiento hacia abajo2
        elif key == 'm' and actual_area2[1] < len(area)-1:
            mover2()
        time.sleep(0.05)

    # volver a calcular la posicion de la raqueta para los rebotes
    actual_area = [area.index('|')]
    actual_area.append(actual_area[0]+1)

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
    elif posibilidades == [1, 2] and not (actual_area[0] == actual[0] or actual_area[1] == actual[0]):
        actual = random_()
        puntos2 += 1
        time.sleep(0.5)
        continue
    elif posibilidades == [0, 3] and not (actual_area2[0] == actual[0] or actual_area2[1] == actual[0]):
        actual = random_()
        puntos += 1
        time.sleep(0.5)
        continue

    else:
        if posibilidades == [1, 2]:
            if actual_area[0] == actual[0]:
                #0
                tipo = 0
            elif actual_area[1] == actual[0]:
                #1
                tipo = 3
        if posibilidades == [0, 3]:
            if actual_area2[0] == actual[0]:
                #0
                tipo = 1
            elif actual_area2[1] == actual[0]:
                #1
                tipo = 2
        tipo_ = movimientos__[tipo]
        posibilidades.remove(tipo_)
        nuevo = movimientos[posibilidades[0]]
        nuevo = [actual[0] + nuevo[0], actual[1] + nuevo[1]]

    tablero[nuevo[0]][nuevo[1]] = 1
    tablero[actual[0]][actual[1]] = 0
    imprimir()