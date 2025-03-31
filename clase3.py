# Uso de operadores aritméticos
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b if b != 0 else "No se puede dividir entre cero"

num = int(input("Ingresa un número: "))

if num > 0:
    print("El número es positivo.")
elif num < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")

edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Puedes entrar al club.")
else:
    print("Lo siento, eres menor de edad y no puedes entrar.")


num = int(input("Ingresa un número: "))

if num >= 0:  # Primera condición: número positivo o cero
    if num == 0:
        print("El número es cero.")
    else:
        print("El número es positivo.")
else:  # Si no es mayor o igual a 0, entonces es negativo
    print("El número es negativo.")
