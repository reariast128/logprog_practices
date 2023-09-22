'''
Ejercicio 10

Realice un programa que calcule la fuerza electroestática entre dos cargas, si se ingresa el valor de las cargas y la distancia entre ellas.
El resultado se debe dar con dos decimales.
'''

constante_coulomb = 9 * 10 ** 9

print("Este programa calcula la fuerza electroestática entre dos cargas, teniendo en cuenta su valor y la distancia entre ellas.")
print("Ten en cuenta de que para introducir decimales tienes que hacerlo usando '.'. Por ejemplo, deberías poner '3.1' en vez de '3,1'")

carga1 = float(input("Introduce el valor de la carga 1, en Coulombs -> "))
carga2 = float(input("Introduce el valor de la carga 2, en Coulombs -> "))
distancia = float(input("Introduce el valor de la distancia que separa las cargas, en metros -> "))


fuerza_electroestatica = round((constante_coulomb * carga1 * carga2) / distancia ** 2, 2)

print(f"\nLa fuerza electroestática entre la carga 1 y la carga 2, separadas a {distancia} unidades de distancia, es de {fuerza_electroestatica}")