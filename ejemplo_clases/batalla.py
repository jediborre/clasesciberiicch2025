#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
from pokemon import Pokemon


class Batalla:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def turno(self):
        if random.choice([True, False]):
            atacante, defensor = self.pokemon1, self.pokemon2
        else:
            atacante, defensor = self.pokemon2, self.pokemon1
        atacante.atacar(defensor)

    def iniciar_batalla(self):
        turno_contador = 1
        while self.pokemon1.esta_vivo() and self.pokemon2.esta_vivo():
            print(f"\n--- Turno {turno_contador} ---")
            self.turno()
            print(f"{self.pokemon1.nombre}: {self.pokemon1.vida} de vida "
                  f"{self.pokemon1.barra_vida()}")
            print(f"{self.pokemon2.nombre}: {self.pokemon2.vida} de vida "
                  f"{self.pokemon2.barra_vida()}")
            turno_contador += 1
        ganador = self.pokemon1 if self.pokemon1.esta_vivo() else self.pokemon2
        perdedor = self.pokemon2 if ganador == self.pokemon1 else self.pokemon1
        print(f"\n¡{ganador.nombre} ha derrotado a {perdedor.nombre}!")
