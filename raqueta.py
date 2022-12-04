import curses
from curses import wrapper

#librerias
from pytimedinput import timedKey
import os
import time

# rows variables
rows = 15
movimientos_area = {'w': -1, 'd': 1}

def main(stdscr):
    # Clear screen
    actual_rows = [rows//2, rows//2+1]
    while True:
        stdscr.clear()

        key, timeout = timedKey(allowCharacters='wdq', timeout=0.1, toprint = False)

        if not timeout:
            if key == 'q':
                print(exit())
            elif (key == 'w' and actual_rows[0]) > 0 or (key == 'd' and actual_rows[1] < rows-1):
                actual_rows = [ actual_rows[0] + movimientos_area[key], actual_rows[1] + movimientos_area[key]]
            time.sleep(0.1)
        
        for row in range(rows):
            if row == actual_rows[0] or row == actual_rows[1]:
                stdscr.addstr('|')
            else:
                stdscr.addstr(' ')
            stdscr.addstr(f'\n')
            
        stdscr.refresh()

wrapper(main)