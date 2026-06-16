"""
El reto: "El juego del número secreto"
El programa debe hacer lo siguiente:

Tener un número secreto ya definido en una variable (por ejemplo, el 7).

Pedirle al usuario que intente adivinar el número.

Si el usuario adivina: Mostrar un mensaje de felicitación y terminar el programa.

Si el usuario falla: Decirle si el número secreto es mayor o menor al que escribió, y dejar que vuelva a intentar.

Tip para empezar: Vas a necesitar un bucle while para que el juego siga corriendo hasta que la persona adivine, y la función input() para recibir lo que escriba el usuario (no olvides convertir ese input a entero con int()).

"""


numero_secreto = 7
numero_usuario = 0
while numero_secreto != numero_usuario: 


    numero_usuario = input("Ingresa tu numero querido: ")

    numero_usuario = int(numero_usuario)

    if numero_secreto > numero_usuario:
        print("El numero secreto es mayor")
    else:
        print("El numero secreto es menor")
    
    if numero_secreto == numero_usuario:
        break