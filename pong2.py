
#librerias
from pytimedinput import timedKey
#   librerias
import os
import time

# tablero y variables
tablero = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ['|', 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
movimientos = {'w': -1, 'd': 1}
opuestos = {'w': 'd', 'd': 'w'}

# funciones

#   imprimir tablero
def imprimir_tablero():
    os.system('cls')
    for tablero_ in tablero:
        print(tablero_)

#   buscar la "raqueta"
def buscar():
    for i in range(len(tablero)):
        if '|' in tablero[i]:
            return i

#   movimientos
def mover():
    nuevo = actual + movimientos[key]
    tablero[actual][0] = 0
    tablero[nuevo][0] = '|'

# codigo
while True:
    actual = buscar()
    key, timeout = timedKey(allowCharacters='wdq', timeout=0.2)
    if not timeout:
        if key == 'q':
            print(exit())
        elif actual == len(tablero)-1:
            if key == 'w':
                mover()
            else:
                nuevo = actual
        elif actual == 0:
            if key == 'd':
                mover()
            else:
                nuevo = actual
        else:
            mover()
        time.sleep(0.1)
    imprimir_tablero()
