#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Pokemon:
    def __init__(self, nombre: str, vida: int, ataque: int, defensa: int):
        self.vida = vida
        self.nombre = nombre
        self.max_vida = vida
        self.ataque = ataque
        self.defensa = defensa

    def esta_vivo(self):
        return self.vida > 0

    def recibir_ataque(self, dano):
        self.vida = max(0, self.vida - dano)

    def calcular_dano(self, oponente):
        dano = self.ataque - oponente.defensa
        return dano if dano > 0 else 1

    def atacar(self, oponente):
        dano = self.calcular_dano(oponente)
        print(f"{self.nombre} ataca a {oponente.nombre} y le hace "
              f"{dano} puntos de daño.")
        oponente.recibir_ataque(dano)

    def barra_vida(self, longitud=20):
        proporcion = self.vida / self.max_vida if self.max_vida else 0
        llenado = int(proporcion * longitud)
        vacio = longitud - llenado
        return "[" + "█" * llenado + "-" * vacio + "]"
