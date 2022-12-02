
#librerias
from pytimedinput import timedKey
import os
import time

# area variables
area = [0, 0, 0, 0, 0, 0, 0, '|', '|', 0, 0, 0, 0, 0, 0, 0, ]
movimientos_area = {'w': -1, 'd': 1}

# funciones area de raqueta
#   imprimir area
def imprimir_area():
    os.system('cls')
    for area_ in area:
        print(area_)
        
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
while True:
    
    actual_area = [area.index('|')]
    actual_area.append(actual_area[0]+1)

    key, timeout = timedKey(allowCharacters='wdq', timeout=0.2)

    if not timeout:
        if key == 'q':
            print(exit())
        elif key == 'w' and actual_area[0] > 0:
            mover()
        elif key == 'd' and actual_area[1] < len(area)-1:
            mover()
        time.sleep(0.1)
    imprimir_area()