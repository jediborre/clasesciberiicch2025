import curses
import time
import os

# Variables globales para almacenar las selecciones
pokemon_retador = None
pokemon_contrincante = None

# Mapeo de colores (ya no se usará para el texto del menú, pero se mantiene por si se requiere) # noqa
COLOR_NAMES = {
    curses.COLOR_YELLOW: "Amarillo",
    curses.COLOR_GREEN: "Verde",
    curses.COLOR_RED: "Rojo",
    curses.COLOR_BLUE: "Azul",
    curses.COLOR_WHITE: "Blanco",
    curses.COLOR_BLACK: "Negro",
}

# Base de datos de pokémons
pokemons = [
    {
        "nombre": "Pikachu",
        "ataque": 55,
        "defensa": 40,
        "color": curses.COLOR_YELLOW,
        "frente": "pikachu_frente.txt",
        "espalda": "pikachu_espalda.txt",
    },
    {
        "nombre": "Bulbasaur",
        "ataque": 49,
        "defensa": 49,
        "color": curses.COLOR_GREEN,
        "frente": "bulbasaur_frente.txt",
        "espalda": "bulbasaur_espalda.txt",
    },
    {
        "nombre": "Charmander",
        "ataque": 52,
        "defensa": 43,
        "color": curses.COLOR_RED,
        "frente": "charmander_frente.txt",
        "espalda": "charmander_espalda.txt",
    },
    {
        "nombre": "Squirtle",
        "ataque": 48,
        "defensa": 65,
        "color": curses.COLOR_BLUE,
        "frente": "squirtle_frente.txt",
        "espalda": "squirtle_espalda.txt",
    },
]


def leer_ascii(ruta):
    """
    Lee el contenido de un archivo de texto ASCII y lo retorna.
    Se asume que la ruta es relativa a la carpeta 'ascii'
    """
    path_completo = os.path.join("ascii", ruta)
    try:
        with open(path_completo, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        return f"Error al leer {ruta}: {e}"


def print_menu(scr, selected_row_idx, menu_items):
    """
    Dibuja el menú en la parte superior central.
    Cada entrada de menú es una tupla:
      - (text_fijo, text_extra, extra_color)
    Si text_extra es None se imprime la línea completa usando el color normal.
    Si se tiene text_extra, se imprime "text_fijo" y luego "text_extra" usando el color extra. # noqa
    El elemento seleccionado se resalta usando A_REVERSE y A_BOLD.
    """
    scr.clear()
    height, width = scr.getmaxyx()
    start_y = 2  # Posición vertical fija

    for idx, item in enumerate(menu_items):
        # Calcular longitud total de la línea
        if item[1] is None:
            total_text = item[0]
        else:
            total_text = item[0] + item[1]
        x = (width - len(total_text)) // 2
        current_y = start_y + idx

        if idx == selected_row_idx:
            scr.attron(curses.A_REVERSE)
            scr.attron(curses.A_BOLD)

        scr.attron(curses.color_pair(2))
        scr.addstr(current_y, x, item[0])
        scr.attroff(curses.color_pair(2))
        if item[1] is not None and item[2] is not None:
            pair_number = 50 if idx == 0 else 51  # 50 para retador, 51 para contrincante # noqa
            curses.init_pair(pair_number, item[2], curses.COLOR_BLACK)
            scr.attron(curses.color_pair(pair_number))
            scr.addstr(current_y, x + len(item[0]), item[1])
            scr.attroff(curses.color_pair(pair_number))
        if idx == selected_row_idx:
            scr.attroff(curses.A_BOLD)
            scr.attroff(curses.A_REVERSE)
    scr.refresh()


def select_pokemon(scr, title):
    """
    Muestra una lista de Pokémon respetando el color configurado en el
    diccionario.
    Cada fila se dibuja usando un par de color específico basado en el valor de 'color'. # noqa
    La fila seleccionada se destaca con A_REVERSE y A_BOLD.
    """
    current_row = 0

    while True:
        scr.clear()
        height, width = scr.getmaxyx()
        x_title = (width - len(title)) // 2
        scr.addstr(1, x_title, title, curses.A_UNDERLINE | curses.A_BOLD)

        for idx, poke in enumerate(pokemons):
            row_text = f"{poke['nombre']} - ATK: {poke['ataque']} DEF: {poke['defensa']}" # noqa
            curses.init_pair(10 + idx, poke["color"], curses.COLOR_BLACK)
            x = (width - len(row_text)) // 2
            y = 3 + idx
            if idx == current_row:
                scr.attron(curses.color_pair(10 + idx))
                scr.attron(curses.A_REVERSE)
                scr.attron(curses.A_BOLD)
                scr.addstr(y, x, row_text)
                scr.attroff(curses.A_BOLD)
                scr.attroff(curses.A_REVERSE)
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


def display_battle(scr, retador, contrincante):
    """
    Muestra la pantalla de batalla:
      - El contrincante se muestra en la esquina superior derecha (imagen frontal). # noqa
      - El retador se muestra en la esquina inferior izquierda (imagen de espalda). # noqa
    Las imágenes se colorean de acuerdo al atributo 'color' del Pokémon.
    Se muestra la pantalla durante 10 segundos.
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

    curses.init_pair(3, contrincante["color"], curses.COLOR_BLACK)
    for idx, line in enumerate(frente_lines):
        y_pos = start_y_frente + idx
        if y_pos < height:
            # Controlar que la línea no se salga del ancho
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

    curses.init_pair(4, retador["color"], curses.COLOR_BLACK)
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


def handle_main_menu_selection(scr, selected_idx):
    global pokemon_retador, pokemon_contrincante
    height, width = scr.getmaxyx()

    if selected_idx == 0:  # Selección de Pokémon Retador
        sel = select_pokemon(scr, "Seleccione Pokémon Retador")
        if sel:
            pokemon_retador = sel

    elif selected_idx == 1:  # Selección de Pokémon Contrincante
        sel = select_pokemon(scr, "Seleccione Pokémon Contrincante")
        if sel:
            pokemon_contrincante = sel

    elif selected_idx == 2:  # Jugar
        scr.clear()
        if not (pokemon_retador and pokemon_contrincante):
            msg = "Debe seleccionar ambos Pokémon antes de jugar"
            x = (width - len(msg)) // 2
            y = height // 2
            scr.addstr(y, x, msg)
            scr.refresh()
            curses.napms(1500)
        else:
            display_battle(scr, pokemon_retador, pokemon_contrincante)

    elif selected_idx == 3:  # Salir
        scr.clear()
        msg = "Saliendo..."
        x = (width - len(msg)) // 2
        y = height // 2
        scr.addstr(y, x, msg)
        scr.refresh()
        curses.napms(1500)


def main(scr):
    global pokemon_retador, pokemon_contrincante

    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)  # Seleccionado
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Normal
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Usado en batalla # noqa

    current_row = 0

    while True:
        # Construir menú principal. Para los dos primeros ítems se arma una tupla: # noqa
        # (texto_fijo, texto_extra, extra_color)
        menu_items = []
        # Ítem 0: Retador
        base_text = "Selección de Pokémon Retador"
        if pokemon_retador:
            # Mostrar solo el nombre del Pokémon entre corchetes
            extra = f" [{pokemon_retador['nombre']}]"
            extra_color = pokemon_retador["color"]
        else:
            extra = ""
            extra_color = None
        menu_items.append((base_text, extra, extra_color))

        # Ítem 1: Contrincante
        base_text = "Selección de Pokémon Contrincante"
        if pokemon_contrincante:
            extra = f" [{pokemon_contrincante['nombre']}]"
            extra_color = pokemon_contrincante["color"]
        else:
            extra = ""
            extra_color = None
        menu_items.append((base_text, extra, extra_color))

        # Ítem 2: Jugar
        if pokemon_retador and pokemon_contrincante:
            menu_items.append(("Jugar", None, None))
        else:
            menu_items.append(("Jugar (Inhabilitado)", None, None))
        # Ítem 3: Salir
        menu_items.append(("Salir", None, None))

        print_menu(scr, current_row, menu_items)
        key = scr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu_items) - 1:
            current_row += 1
        elif key in [curses.KEY_ENTER, 10, 13]:
            if menu_items[current_row][0].startswith("Jugar (Inhabilitado)"):
                continue
            handle_main_menu_selection(scr, current_row)
            if current_row == len(menu_items) - 1:
                break


if __name__ == "__main__":
    curses.wrapper(main)
