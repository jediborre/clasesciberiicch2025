import curses
import time
from ascii_helper import leer_ascii
from constants import COLOR_BLACK


def display_battle(scr, retador, contrincante):
    """
    Muestra la pantalla de batalla:
     - El contrincante se muestra en la esquina superior derecha (img frontal).
     - El retador se muestra en la esquina inferior izquierda (img de espalda).
    Las imágenes se colorean de acuerdo al atributo 'color' del Pokémon.
    La pantalla se muestra durante 10 segundos.
    """
    scr.clear()
    height, width = scr.getmaxyx()

    ascii_frente = leer_ascii(contrincante["frente"])
    ascii_espalda = leer_ascii(retador["espalda"])

    frente_lines = ascii_frente.strip("\n").splitlines()
    espalda_lines = ascii_espalda.strip("\n").splitlines()

    start_y_frente = 1
    max_width_frente = max((len(line) for line in frente_lines), default=0)
    start_x_frente = width - max_width_frente - 1

    curses.init_pair(3, contrincante["color"], COLOR_BLACK)
    for idx, line in enumerate(frente_lines):
        y_pos = start_y_frente + idx
        if y_pos < height:
            line = line[:max(0, width - start_x_frente)]
            try:
                scr.attron(curses.color_pair(3))
                scr.addstr(y_pos, start_x_frente, line)
                scr.attroff(curses.color_pair(3))
            except curses.error:
                pass

    max_width_espalda = max((len(line) for line in espalda_lines), default=0) # noqa
    start_y_espalda = height - len(espalda_lines) - 1
    start_x_espalda = 1

    curses.init_pair(4, retador["color"], COLOR_BLACK)
    for idx, line in enumerate(espalda_lines):
        y_pos = start_y_espalda + idx
        if y_pos < height:
            line = line[:max(0, width - start_x_espalda)]
            try:
                scr.attron(curses.color_pair(4))
                scr.addstr(y_pos, start_x_espalda, line)
                scr.attroff(curses.color_pair(4))
            except curses.error:
                pass

    scr.refresh()
    time.sleep(10)
