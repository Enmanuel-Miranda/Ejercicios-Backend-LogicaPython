# ==============================================================================
# EJERCICIO DE PYTHON - NIVEL INICIACIÓN: CONTROL DE ACCESO A EVENTO 🎟️
# ==============================================================================
# Gabriel, escribe tu solución completa desde cero aquí abajo.
#
# OBJETIVO:
# Crea un programa para una ticketera que determine si una persona puede ingresar
# a un evento VIP y si debe pagar un cargo extra por pase tardío.
#
# REGLAS DEL NEGOCIO:
# 1. Define tres variables: 
#    - 'edad' (un número entero, ej. 20)
#    - 'tiene_entrada' (un booleano: True o False)
#    - 'hora_llegada' (un número entero en formato 24h, ej. 23 para las 11 PM)
# 2. Evalúa las siguientes condiciones con lógica booleana y condicionales:
#    - Para entrar, la persona DEBE ser mayor de edad (18 años o más) Y tener entrada.
#    - Si cumple lo anterior y llega DESPUÉS de las 22 (10 PM), entra pero paga un 
#      cargo extra de $15. Si llega a las 22 o antes, el cargo extra es $0.
#    - Si no cumple los requisitos de edad o entrada, el acceso es denegado.
# 3. Imprime el resultado final:
#    - Si entra: "ACCESO CONCEDIDO. Cargo por pase tardío: $X" (donde X es el cargo).
#    - Si no entra: "ACCESO DENEGADO."
#
# Escribe todo tu código a partir de aquí abajo:
# ==============================================================================


# Variables a utilizar
edad = 20
tiene_entrada = True
hora_llegada = 22


cargo = 0
acceso = ""

if edad >= 18 and tiene_entrada ==  True:

    cargo_extra = ""
    if hora_llegada > 22:
        cargo += 15
        cargo_extra = f"Cargo por pase tardio: ${cargo}"

    acceso = "ACCESO CONCEDIDO"


else:
    acceso = "ACCESO DENEGADO"



print("\n----------------\n")

print(acceso, cargo_extra)


print("\n----------------\n")




