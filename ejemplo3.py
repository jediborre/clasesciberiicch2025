semaforo = input("Como ves el semaforo\n")
semaforo = semaforo.lower()

if semaforo in ["verde",
                "VERDE",
                " VERDE",
                "VERDE ",
                " verde",
                "verde ",
                "verrrrr   "]:
    print("avanzando")
elif semaforo == "amarillo":
    print("Reducir Velocidad")
else:
    print("Alto")
