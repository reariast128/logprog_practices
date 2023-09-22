'''
Ejercicio 6

Escriba un programa que permita calcula la distancia euclidiana entre dos puntos si 
se ingresan sus coordenadas. El resultado se debe dar con dos decimales. 
'''

print("Este programa calcula la distancia euclidiana entre dos puntos (x0, y0) y (x1, y1).")

x0 = float(input("Introduce el valor de x0 -> "))
y0 = float(input("Introduce el valor de y0 -> "))
x1 = float(input("Introduce el valor de x1 -> "))
y1 = float(input("Introduce el valor de y1 -> "))

distancia_euclidiana = round(((x1 - x0) ** 2 + (y1 - y0) ** 2) ** (1/2), 2)

print(f"La distancia euclidiana entre ({x0}, {y0} y ({x1}, {y1}) es {distancia_euclidiana}")