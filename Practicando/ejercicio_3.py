
"""
El reto: "El filtro del carrito de compras"
Imagina que tienes una lista con los precios de varios productos que un cliente quiere comprar en una tienda online. Tu trabajo es aplicar un descuento automático, pero solo a los productos que sean caros.

Lo que debe hacer tu programa:

Crea una lista llamada precios que contenga los siguientes números: [10, 55, 8, 120, 32, 75, 4].

El programa debe recorrer esa lista uno a uno (pista: usa un bucle for).

Si el producto cuesta 50 o más, debes aplicarle un 10% de descuento y mostrar en pantalla el nuevo precio rebajado.

Si el producto cuesta menos de 50, muéstralo en pantalla con su precio original (sin descuento).

Tip para empezar: Para calcular el precio con el 10% de descuento, puedes multiplicar el precio original por 0.9.

"""

precios = [10, 55, 8, 120, 32, 75, 4]


#print("Hello World")
print("\nListanddo el precio de los productos \n")

for precio in precios:
    if precio > 50:
        precio =  ( precio * 0.9)
        print(precio)
    else:
        print(precio)