'''
Ejercicio 1

Escriba un programa que solicite al usuario una temperatura Celsius, convierta la 
temperatura a Fahrenheit y Kelvin e imprima la temperatura convertida. Utilice 
format para mejorar la salida. El valor es ## °F y equivalente a ## K

'''

print("Este programa calcula grados celcius en grados Farenheit y en grados Kelvin")
grados_celcius = float(input("Por favor, introduce los grados a transformar en celcius -> "))

grados_farenheit = grados_celcius * (9/5) + 32
grados_kelvin = grados_celcius + 273

print(f"Los grados que introduciste, transformados a Farenheit, son {grados_farenheit} ºF")
print(f"Los grados que introduciste, transformados a Farenheit, son {grados_kelvin} K")