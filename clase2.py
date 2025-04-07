# Tipo de dato entero (int)
numero_entero = 42
numeroentero = 42
# Tipo de dato flotante (float)
numero_flotante = 3.14

# Tipo de dato cadena de texto (str)
cadena = "Hola, Mundo"

# Tipo de dato booleano (bool)
es_verdadero = True
es_falso = False

# Tipo de dato lista (list)
lista = []
lista = [1, 2, 3, "cuatro", 5.6, [], {}]

# Tipo de dato tupla (tuple)
trupla = ()
tupla = (1, 2, 3)

# Tipo de dato conjunto (set)
conjunto = {1, 2, 3, 4, 5, 5}

# Tipo de dato diccionario (dict)
diccionario = {}
diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "genero": "quimera",
    "calificaciones": {
        "matematicas": 10,
        "cibernetica": 10
    },
    "calificaciones1": [
        ["matematicas", 10],
        ["cibernetica", 9]
    ]

}
alumno = {"nombre": "Fernando", "edad": 38}


# Tipo de dato None (NoneType)
nada = None

# Imprimiendo los tipos de datos y sus valores
print("Número entero:", numero_entero, ", Tipo:", type(numero_entero))
print("Número flotante:", numero_flotante, ", Tipo:", type(numero_flotante))
print("Cadena de texto:", cadena, ", Tipo:", type(cadena))
print("Booleano (True):", es_verdadero, ", Tipo:", type(es_verdadero))
print("Booleano (False):", es_falso, ", Tipo:", type(es_falso))
print("Lista:", lista, ", Tipo:", type(lista))
print("Tupla:", tupla, ", Tipo:", type(tupla))
print("Conjunto:", conjunto, ", Tipo:", type(conjunto))
print("Diccionario:", diccionario, ", Tipo:", type(diccionario))
print("None:", nada, ", Tipo:", type(nada))
