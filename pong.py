import random as rn
import os
import time
import curses
from curses import wrapper
from pytimedinput import timedKey

TIME = 0.05

MENSAJE = """
        __________    ____________  _____    _____  ____________
       |          \  /            \|     \  |     |/	        \\
       |     __    \|     ____     |      \ |     |      ___     |
       |    |  \    |    /    \    |       \|     |     /   \____|
       |    |   |   |    |    |    |              |    |  ______
       |    |__/    |    |    |    |              |    | |      \\
       |           /|    |    |    |              |    | |__     |
       |     _____/ |    |    |    |              |    |    |    |
       |    |       |    \____/    |     |\       |     \__/     | 
       |    |       |              |     | \      |              |
       |____|        \____________/|_____|  \_____|\____________/

								@lipezj
								@Lpe_47
"""

tablero = [10, 26]
rows = tablero[0]
movimientos = {
    0: [-1, -1], 1: [-1, 1], 
    2: [1, 1], 3: [1, -1],
    4: [0, 1], 5: [0, -1]
}
movimientos_ = {
    "-1-1": 0, "-11": 1,
    "1-1": 3, "11": 2,
    "01": 4, "0-1": 5,
    "00":6
}
movimientos__ = [2,3,0,1,5,4]
movimientos_area = {'w': -1, 'd': 1, 'k': -1, 'm': 1}
movimiento_recto = [[0,3,5],[1,2,4]]
puntos_g = [0, 0]

def start():
    os.system('cls')
    print(MENSAJE)
    if sum(puntos_g) > 0:
        print(f'Victorias: {puntos_g[0]} - {puntos_g[1]}\n')
    else:
        print('jugador 1: w, d')
        print(f'jugador 2: k, m\n')
    print('(ctrl + c para salir)')
    input('Presiona enter para comenzar ')
    os.system('cls')

def imprimir_tablero(stdscr, nuevo, actual_rows1, actual_rows2, puntos):
    try:
        stdscr.addstr('x'*(tablero[1]+1) + f'\n')
        for row in range(tablero[0]):
            if row == actual_rows1[0] or row == actual_rows1[1]:
                    stdscr.addstr('|')
            else:
                stdscr.addstr(' ')
            if nuevo[0] == row:
                stdscr.addstr((' '*(nuevo[1])) + 'O' + ' '*(tablero[1]-(nuevo[1]+1)))
            else:
                stdscr.addstr(' '*(tablero[1]))
            if row == actual_rows2[0] or row == actual_rows2[1]:
                    stdscr.addstr('|')
            else:
                stdscr.addstr(' ')
            stdscr.addstr(f'\n')
        stdscr.addstr('x'*(tablero[1]+1))
        stdscr.addstr(f'\n {puntos[0]} - {puntos[1]}')
        time.sleep(0.03)
    except:
        print('', end='')

def posibilidades_(actual):
    if (actual[0] == 0 and actual[1] == 0) or (actual[0] == 0 and actual[1] == tablero[1]-1) or (actual[0] == tablero[0]-1 and actual[1] == 0) or (actual[0] == tablero[0]-1 and actual[1] == tablero[1]-1):
        return [6]
    if actual[0] == tablero[0]-1:
        return [0, 1]
    elif actual[0] == 0:
        return [2, 3]
    elif actual[1] == tablero[1]-1:
        return [0, 3, 5]
    elif actual[1] == 0:
        return [1, 2, 4]
    else:
        return [0,1,2,3]

def rebote_pared(tipo, tipo_, posibilidades):
    tipo__ = rn.choice(tipo_)
    tipo_.remove(tipo__)
    tipo = rn.choice(tipo_)
    posibilidades.remove(movimientos__[tipo__])
    return tipo

def main(stdscr):

    actual_rows1 = [rows//2, rows//2+1]
    actual_rows2 = [rows//2, rows//2+1]
    nuevo = [rn.randint(0, tablero[0]-1), tablero[1]//2]
    actual = nuevo
    puntos = [0, 0]
    timeout_count = 0

    while True:
        stdscr.clear()

        anterior = actual
        actual = nuevo

        #calcular el tipo de movimiento anterior
        tipo = movimientos_[str(actual[0] - anterior[0]) + str(actual[1] - anterior[1])]
        #ejecutar la funcion para saber cuantas posibilidades hay en el movimiento
        posibilidades = posibilidades_(actual)

        #teclas
        time_trans = time.time()
        key, timeout = timedKey(allowCharacters='wdqkm', timeout=TIME, toprint=False)

        if not timeout:
            timeout_count = time.time() - time_trans
            if key == 'q':
                print(exit())

            if (key == 'w' and actual_rows1[0] > 0) or (key == 'd' and actual_rows1[1] < rows-1):
                actual_rows1 = [ actual_rows1[0] + movimientos_area[key], actual_rows1[1] + movimientos_area[key]]

            if (key == 'k' and actual_rows2[0] > 0) or (key == 'm' and actual_rows2[1] < rows-1):
                actual_rows2 = [ actual_rows2[0] + movimientos_area[key], actual_rows2[1] + movimientos_area[key]]
            time.sleep(timeout_count - (timeout_count - TIME))

        if 10 in puntos:
            os.system('cls')
            if puntos[0] == 10: 
                print()(f'\n Ganaste! jugador 1 \n')
                puntos_g[0] += 1
            else: 
                print(f'\n Ganaste! jugador 2 \n')
                puntos_g[1] += 1
            break

        #primer movimiento
        if actual == anterior:
            posibilidad = rn.choice(posibilidades)
            nuevo = [actual[0] + (movimientos[posibilidad][0]), actual[1] + (movimientos[posibilidad][0])]
        #esquinas
        elif len(posibilidades) == 1:
            if ((actual[0] == actual_rows1[0] or actual[0] == actual_rows1[1]) and tipo in [0,3]) or ((actual_rows2[0] == actual[0] or actual_rows2[1] == actual[0]) and tipo in [1,2]):
                nuevo = anterior
            elif not (actual[0] == actual_rows1[0] or actual[0] == actual_rows1[1]):
                nuevo = [rn.randint(0, tablero[0]-1), tablero[1]//2]
                actual = nuevo
                puntos[1] += 1
            elif not (actual_rows2[0] == actual[0] or actual_rows2[1] == actual[0]):
                nuevo = [rn.randint(0, tablero[0]-1), tablero[1]//2]
                actual = nuevo
                puntos[0] += 1
        #movimiento normal
        elif len(posibilidades) == 4:
            nuevo = [actual[0] + (actual[0] - anterior[0]), actual[1] + (actual[1] - anterior[1])]

        elif posibilidades == [1, 2, 4] and not (actual_rows1[0] == actual[0] or actual_rows1[1] == actual[0]):
            nuevo = [rn.randint(0, tablero[0]-1), tablero[1]//2]
            actual = nuevo
            puntos[1] += 1
        elif posibilidades == [0, 3, 5] and not (actual_rows2[0] == actual[0] or actual_rows2[1] == actual[0]):
            nuevo = [rn.randint(0, tablero[0]-1), tablero[1]//2]
            actual = nuevo
            puntos[0] += 1

        #rebotes
        else:
            if (actual_rows1[0] == actual[0] or actual_rows1[1] == actual[0]) and posibilidades == [1, 2, 4]:
                tipo = rebote_pared(tipo, [0,3,5], posibilidades)
                
            if (actual_rows2[0] == actual[0] or actual_rows2[1] == actual[0]) and posibilidades == [0, 3, 5]:
                tipo = rebote_pared(tipo, [1,2,4], posibilidades)
                    
            posibilidades.remove(movimientos__[tipo])
            nuevo = [actual[0] + movimientos[posibilidades[0]][0], actual[1] + movimientos[posibilidades[0]][1]]

        imprimir_tablero(stdscr, nuevo, actual_rows1, actual_rows2, puntos)
        stdscr.refresh()

while True: 
    start()
    wrapper(main)
    curses.endwin()