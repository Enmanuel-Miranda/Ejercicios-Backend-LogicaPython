"""
El reto: "El generador de nombres de usuario"
Imagina que estás creando el sistema de registro para una plataforma y necesitas crear automáticamente un nombre de usuario (username) para los nuevos miembros basado en su nombre y apellido.

Lo que debe hacer tu programa:

Pedir al usuario que ingrese su nombre (por ejemplo: "Carlos").

Pedir al usuario que ingrese su apellido (por ejemplo: "Mendoza").

El programa debe generar y mostrar un nombre de usuario combinando:

Las tres primeras letras del nombre en minúsculas.

Las tres primeras letras del apellido en minúsculas.

Un número aleatorio al final (puedes usar un número fijo como 123 para no complicarte con librerías, o investigar cómo usar random).

Ejemplo de resultado: Si el usuario es Carlos Mendoza, el programa debería imprimir algo como: carmen123.

Tip para empezar: En Python puedes cortar textos (hacer slicing) usando corchetes, por ejemplo: texto[0:3] te da las tres primeras letras. Y para pasarlo a minúsculas, puedes usar el método .lower()
"""

import random

print("\n INGRESE SUS NOMBRES Y APELLIDOS \n")

nombre = input("Ingrese su nombre: ")

apellido = input("Ingrese su apellido: ")

if len(nombre) < 4 or len(apellido) <4:
    print("\nVuelva a ingresar el nombre o el apellido\n")
else:

    nom_3 = nombre[0:3].lower()
    ape = apellido[0:3].lower()

    numeros = ""

    for valor in range(3):
        numero = round(random.random() * 10)
        numeros += str(numero)

    print("\n")

    usuario = f"{nom_3}{ape}{numeros}"

    print(f"Su usuario es {usuario}\n")
