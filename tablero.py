import random as rn
import os
import time
from pytimedinput import timedKey
import curses
from curses import wrapper

def imprimir_tablero(stdscr, nuevo):
    stdscr.addstr('x'*tablero[1] + f'\n')
    for i in range(tablero[0]):
        if nuevo[0] == i:
            stdscr.addstr((' '*(nuevo[1]-1)) + 'O' + ' '*(tablero[1]-nuevo[1]))
        else:
            stdscr.addstr(' '*tablero[1])
        stdscr.addstr(f'\n')
    stdscr.addstr('x'*tablero[1])
    time.sleep(0.02)

def posibilidades_(actual):
    if (actual[0] == 0 and actual[1] == 0) or (actual[0] == 0 and actual[1] == tablero[1]-1) or (actual[0] == tablero[0]-1 and actual[1] == 0) or (actual[0] == tablero[0]-1 and actual[1] == tablero[1]-1):
        return [4]
    if actual[0] == tablero[0]-1:
        posibilidades_ = [0, 1]
    elif actual[0] == 0:
        posibilidades_ = [2, 3]
    elif actual[1] == tablero[1]-1:
        posibilidades_ = [0, 3]
    elif actual[1] == 0:
        posibilidades_ = [1, 2]
    else:
        posibilidades_ = [0,1,2,3]
    return posibilidades_

tablero = [15, 40]
movimientos = {
    0: [-1, -1], 1: [-1, 1], 
    2: [1, 1], 3: [1, -1]
}
movimientos_ = {
    "-1-1": 0, "-11": 1,
    "1-1": 3, "11": 2,
    "00": 4
}
movimientos__ = {0: 2, 1: 3, 2: 0, 3: 1}

def main(stdscr):

    nuevo = [rn.randint(0, tablero[0]-1), tablero[1]//2]
    actual = nuevo

    while True:
        stdscr.clear()

        #teclas
        key, outtime = timedKey(allowCharacters='q', timeout=0.05, toprint=False)
        if key == 'q':
            print(exit())

        anterior = actual
        actual = nuevo
        #calcular el tipo de movimiento anterior
        tipo = movimientos_[str(actual[0] - anterior[0]) + str(actual[1] - anterior[1])]
        #ejecutar la funcion para saber cuantas posibilidades hay en el movimiento
        posibilidades = posibilidades_(actual)

        #primer movimiento
        if actual == anterior:
            posibilidad = rn.choice(posibilidades)
            nuevo = [actual[0] + (movimientos[posibilidad][0]), actual[1] + (movimientos[posibilidad][0])]
        #esquinas
        elif posibilidades[0] == 4:
            nuevo = anterior
        #movimientto normal
        elif len(posibilidades) == 4:
            nuevo = [actual[0] + (actual[0] - anterior[0]), actual[1] + (actual[1] - anterior[1])]
        #rebotes
        else:
            posibilidades.remove(movimientos__[tipo])
            nuevo = [actual[0] + movimientos[posibilidades[0]][0], actual[1] + movimientos[posibilidades[0]][1]]

        imprimir_tablero(stdscr, nuevo)
        stdscr.refresh()

wrapper(main)