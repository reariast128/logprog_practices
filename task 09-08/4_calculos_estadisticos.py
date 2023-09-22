'''
Ejercicio 4

Escriba un programa que dados 5 números (ingresados por el usuario) calcule el 
promedio, la varianza, la desviación estándar y el coeficiente de variación.
'''

print("Este es un programa que calcule el promedio, la varianza, la desviación estándar y el coeficiente de variación de un número.")
n1 = float(input("Por favor, introduce el primer número -> "))
n2 = float(input("Por favor, introduce el segundo número -> "))
n3 = float(input("Por favor, introduce el tercer número -> "))
n4 = float(input("Por favor, introduce el cuarto número -> "))
n5 = float(input("Por favor, introduce el quinto número -> "))

decimales_precision = 3

promedio = round((n1 + n2 + n3 + n4 + n5) / 5, decimales_precision)
varianza = round(((n1 + promedio) ** 2 + (n2 + promedio) ** 2 + (n3 + promedio) ** 2 + (n4 + promedio) ** 2 + (n5 + promedio) ** 2)/5, decimales_precision) # Representar la salida como unidades de medida al cuadrado
desviacion_estandar = round(varianza ** (1/2), decimales_precision)
coeficiente_variacion = round((desviacion_estandar / promedio) * 100, decimales_precision)

print("-" * 25)
print(f"El promedio es igual a {promedio}, la varianza es de {varianza}, la desviación estándar es de {desviacion_estandar}, y el coeficiente de variación es igual a {coeficiente_variacion}")