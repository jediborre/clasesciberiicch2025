import curses
from menu import print_menu, select_pokemon
from battle import display_battle
from constants import COLOR_BLACK, COLOR_WHITE

# Variables globales para almacenar las selecciones
pokemon_retador = None
pokemon_contrincante = None


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
    curses.init_pair(1, COLOR_BLACK, COLOR_WHITE)  # Seleccionado
    curses.init_pair(2, COLOR_WHITE, COLOR_BLACK)  # Normal
    curses.init_pair(3, COLOR_WHITE, COLOR_BLACK)  # Usado en batalla

    current_row = 0

    while True:
        # Construir menú principal.
        menu_items = []
        base_text = "Selección de Pokémon Retador"
        if pokemon_retador:
            extra = f" [{pokemon_retador['nombre']}]"
            extra_color = pokemon_retador["color"]
        else:
            extra = ""
            extra_color = None
        menu_items.append((base_text, extra, extra_color))

        base_text = "Selección de Pokémon Contrincante"
        if pokemon_contrincante:
            extra = f" [{pokemon_contrincante['nombre']}]"
            extra_color = pokemon_contrincante["color"]
        else:
            extra = ""
            extra_color = None
        menu_items.append((base_text, extra, extra_color))

        if pokemon_retador and pokemon_contrincante:
            menu_items.append(("Jugar", None, None))
        else:
            menu_items.append(("Jugar (Inhabilitado)", None, None))
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
