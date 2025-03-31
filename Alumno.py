class Alumno:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f'Hola! Soy {self.nombre}, tengo {self.edad}')
