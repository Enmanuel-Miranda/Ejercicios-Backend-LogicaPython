# ==============================================================================
# EJERCICIO DE PYTHON - NIVEL INICIACIÓN: CONTROL DE ENVÍOS 🚚
# ==============================================================================
# Gabriel, escribe tu solución completa desde cero aquí abajo.
#
# OBJETIVO:
# Crea un programa que calcule e imprima en pantalla el costo de envío.
#
# REGLAS DEL NEGOCIO:
# 1. Define una variable con el monto de la compra (ej. 65.50, 32.00, etc.).
# 2. Usa un condicional (if / else) para evaluar:
#    - Si la compra es igual o mayor a 50, el costo de envío es $0.
#    - Si la compra es menor a 50, el costo de envío es $10.
# 3. Imprime un mensaje claro que muestre el monto de la compra y el costo final de envío.
#
# Escribe todo tu código a partir de aquí abajo:
# ==============================================================================


monto = 15
envio = 0
if monto >= 50:
    envio = 0
else:
    envio = 10

m_total = monto + envio

print("\nCoste de envio")

print(f"\nEl monto de la compra sera de: {monto}")
print(f"El monto total a pagar sera de: {m_total}")

