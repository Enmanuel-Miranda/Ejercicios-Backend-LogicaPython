# ==============================================================================
# EJERCICIO DE PYTHON - BÁSICO AVANZADO: MONITOR DE TEMPERATURAS DE SERVIDORES 🖥️
# ==============================================================================
# Gabriel, escribe tu solución completa desde cero aquí abajo.
#
# OBJETIVO:
# Crea un programa que analice una lista de temperaturas registradas en un data 
# center para detectar alertas de sobrecalentamiento y calcular el promedio.
#
# REGLAS DEL NEGOCIO:
# 1. Define una lista llamada 'temperaturas' con los siguientes valores:
#    [22.5, 26.0, 31.2, 19.8, 28.5, 30.0, 24.1]
# 2. El programa debe recorrer la lista usando un bucle (for) y hacer dos cosas:
#    - Calcular la suma total de las temperaturas para obtener el promedio después.
#    - Contar cuántas temperaturas superan el límite de seguridad (28.0 grados o más).
# 3. Al finalizar el bucle, calcula el promedio (Suma total / Cantidad de registros).
# 4. Imprime en pantalla un reporte con:
#    - El promedio de temperatura (redondeado a 1 decimal).
#    - La cantidad total de alertas por sobrecalentamiento detectadas.
#
# Escribe todo tu código a partir de aquí abajo:
# ==============================================================================
temperaturas = [22.5, 26.0, 31.2, 19.8, 28.5, 30.0, 24.1]
temperatura_suma = 0
temperatura_cantidad = len(temperaturas)
temperaturas_max = 0

for temp in temperaturas:
    temperatura_suma += temp
    if temp >= 28.0:
        temperaturas_max +=1

promedio = temperatura_suma / temperatura_cantidad

print(f"\nEl promedio de temperaturas es de: {round(promedio,1)}")
print(f"Cantidad de temperaturas que superan los 28: {temperaturas_max}\n")