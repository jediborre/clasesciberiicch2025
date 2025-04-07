python3 -m venv env
source env/bin/activate

<!-- comando para instalar Libreria Textual -->
<!-- comando para instalar Libreria Textual -->
python -m pip install textual textual-dev

<!-- comando para instalar Libreria pygame -->
pip install pygame

<!-- comando para instalar Libreria Arcade -->
pip install arcade


<!-- Librerias adicionales de C para curses, en teoria ya deberia venir en curses -->
sudo apt-get update
sudo apt-get install libncurses5-dev libncursesw5-dev
<!-- comando para instalar Libreria Curses para codespaces -->
pip install curses

<!-- comando para instalar Libreria Curses para Windows-->
pip install windows-curses

Referencia Pokemon
https://www.pokemon.com/

Referencias Imagenes
https://pokemon-opalo.fandom.com/
https://www.wikidex.net/wiki/

Referencia Imagen a ASCII
https://codepen.io/Mikhail-Bespalov/pen/JoPqYrz

menu_pokemon_dividido/
├── ascii/
│   ├── pikachu_frente.txt
│   ├── pikachu_espalda.txt
│   ├── bulbasaur_frente.txt
│   ├── bulbasaur_espalda.txt
│   └── ... (resto de archivos ASCII)
├── battle.py
├── constants.py
├── main.py
├── menu.py
├── pokemon.py
└── ascii_helper.py