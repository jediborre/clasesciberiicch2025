#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pokemon import Pokemon
from batalla import Batalla


def main():
    pikachu = Pokemon("Pikachu", vida=35, ataque=55, defensa=40)
    bulbasaur = Pokemon("Bulbasaur", vida=45, ataque=49, defensa=49)
    batalla = Batalla(pikachu, bulbasaur)
    batalla.iniciar_batalla()


if __name__ == "__main__":
    main()
