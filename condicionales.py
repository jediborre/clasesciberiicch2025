# Condicionales en Python

# Estructura Condicional
# Sintaxis: if condicion:
#                bloque_de_codigo
#            elif otra_condicion:
#                bloque_de_codigo
#            else:
#                bloque_de_codigo
# Ejemplo
edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print("Puedes entrar al club.")
elif edad >= 12:
    print("Eres un adolescente.")
else:
    print("Eres un niño.")
# Ejemplo de uso de operadores lógicos
# Sintaxis: if condicion1 and condicion2:
#                bloque_de_codigo
#            elif condicion1 or condicion2:
#                bloque_de_codigo
#            else:
#                bloque_de_codigo
# Ejemplo
edad = int(input("Ingresa tu edad: "))
if edad >= 18 and edad < 60:
    print("Eres un adulto.")
elif edad >= 60:
    print("Eres un anciano.")
else:
    print("Eres un niño o adolescente.")
# Ejemplo de uso de operadores de comparación
# Sintaxis: if variable1 == variable2:
#                bloque_de_codigo
#            elif variable1 != variable2:
#                bloque_de_codigo
#            else:
#                bloque_de_codigo
# Ejemplo
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
if numero1 == numero2:
    print("Los números son iguales.")
elif numero1 != numero2:
    print("Los números son diferentes.")
# Ejemplo de uso de operadores de comparación
# Sintaxis: if variable1 < variable2:
#                bloque_de_codigo
#            elif variable1 > variable2:
#                bloque_de_codigo
#            else:
#                bloque_de_codigo
# Ejemplo
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
if numero1 < numero2:
    print("El primer número es menor que el segundo.")
elif numero1 > numero2:
    print("El primer número es mayor que el segundo.")
else:
    print("Los números son iguales.")
# Ejemplo de uso de operadores de comparación
# Sintaxis: if variable1 <= variable2:
#                bloque_de_codigo
#            elif variable1 >= variable2:
#                bloque_de_codigo
#            else:
#                bloque_de_codigo
# Ejemplo
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
if numero1 <= numero2:
    print("El primer número es menor o igual que el segundo.")
elif numero1 >= numero2:
    print("El primer número es mayor o igual que el segundo.")
# else:
#     print("Los números son iguales.")


# Operadores Ternarios
# Sintaxis: variable = valor_si_verdadero if condicion else valor_si_falso
# Ejemplo
condicion = True
valor_si_verdadero = "Es verdadero"
valor_si_falso = "Es falso"
# Asignación de valor usando operador ternario
variable = valor_si_verdadero if condicion else valor_si_falso

# Ejemplo de uso de operadores ternarios
edad = int(input("Ingresa tu edad: "))
mensaje = "Puedes entrar al club." if edad >= 18 else "Lo siento, eres menor de edad y no puedes entrar." # noqa
print(mensaje)
