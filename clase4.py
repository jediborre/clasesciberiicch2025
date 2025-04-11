alumno = {
    "nombre": "Fernando Borrego",
    "edad": 20,
    "materia": "Cibernética II",
    "calificaciones": [7.5, 8.0, 9.0]
}

print("Nombre:", alumno["nombre"])
print("Edad:", alumno["edad"])
print("Materia:", alumno["materia"])
print("Calificaciones:", alumno["calificaciones"])


class Alumno:
    def __init__(self, nombre, edad, materia, calificaciones):
        self.nombre = nombre
        self.edad = edad
        self.materia = materia
        self.calificaciones = calificaciones

    def promedio(self):
        return sum(self.calificaciones) / len(self.calificaciones) if self.calificaciones else 0 # noqa

    def __str__(self):
        return (f"Alumno: {self.nombre}, Edad: {self.edad}, "
                f"materia: {self.materia}, Promedio: {self.promedio():.2f}")


obj_alumno = Alumno("Fernando Borrego", 20, "Cibernética II", [7.5, 8.0, 9.0])

print(obj_alumno)
