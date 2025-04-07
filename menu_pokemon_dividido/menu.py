import curses
from pokemon import pokemons
from constants import COLOR_BLACK, REVERSE, BOLD, UNDERLINE


def print_menu(scr, selected_row_idx, menu_items):
    """
    Dibuja el menú en la parte superior central.
    Cada entrada de menú es una tupla:
      - (texto_fijo, texto_extra, extra_color)
    Si texto_extra es None se imprime la línea completa usando el color normal.
    Si existe texto_extra, se imprime "texto_fijo" y luego "texto_extra"
    usando el color extra.
    El elemento seleccionado se resalta usando REVERSE y BOLD.
    """
    scr.clear()
    height, width = scr.getmaxyx()
    start_y = 2  # Posición vertical fija

    for idx, item in enumerate(menu_items):
        total_text = item[0] if item[1] is None else item[0] + item[1]
        x = (width - len(total_text)) // 2
        current_y = start_y + idx

        if idx == selected_row_idx:
            scr.attron(REVERSE)
            scr.attron(BOLD)

        scr.attron(curses.color_pair(2))
        scr.addstr(current_y, x, item[0])
        scr.attroff(curses.color_pair(2))
        if item[1] is not None and item[2] is not None:
            pair_number = 50 if idx == 0 else 51
            curses.init_pair(pair_number, item[2], COLOR_BLACK)
            scr.attron(curses.color_pair(pair_number))
            scr.addstr(current_y, x + len(item[0]), item[1])
            scr.attroff(curses.color_pair(pair_number))
        if idx == selected_row_idx:
            scr.attroff(BOLD)
            scr.attroff(REVERSE)
    scr.refresh()


def select_pokemon(scr, title):
    """
    Muestra una lista de Pokémon con su color configurado.
    Cada fila se dibuja usando un par de color específico
    basado en el atributo 'color'. La fila seleccionada se
    destaca con REVERSE y BOLD.
    """
    current_row = 0

    while True:
        scr.clear()
        height, width = scr.getmaxyx()
        x_title = (width - len(title)) // 2
        scr.addstr(1, x_title, title, UNDERLINE | BOLD)

        for idx, poke in enumerate(pokemons):
            row_text = f"{poke['nombre']} - ATK: {poke['ataque']} DEF: {poke['defensa']}" # noqa
            curses.init_pair(10 + idx, poke["color"], COLOR_BLACK)
            x = (width - len(row_text)) // 2
            y = 3 + idx
            if idx == current_row:
                scr.attron(curses.color_pair(10 + idx))
                scr.attron(REVERSE)
                scr.attron(BOLD)
                scr.addstr(y, x, row_text)
                scr.attroff(BOLD)
                scr.attroff(REVERSE)
                scr.attroff(curses.color_pair(10 + idx))
            else:
                scr.attron(curses.color_pair(10 + idx))
                scr.addstr(y, x, row_text)
                scr.attroff(curses.color_pair(10 + idx))
        scr.refresh()

        key = scr.getch()
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(pokemons) - 1:
            current_row += 1
        elif key in [curses.KEY_ENTER, 10, 13]:
            return pokemons[current_row]
        elif key == 27:  # ESC para cancelar
            return None
