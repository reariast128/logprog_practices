'''
Ejercicio 2

Escriba un programa al que se le ingrese un valor cualquiera entre 1000 y 999999
y escriba ese mismo número, pero utilizando coma para los miles y signo pesos. Por 
ejemplo, se ingrese 20000 y la salida sea $20,000. 
'''

print("Este programa representa un número en formato de pesos.")
print("Por ejemplo, el número 123456 lo representa como $123,456")

valor = int(input("Por favor, introduce un valor entre 1000 y 999999 -> "))

representacion_valor = f"${valor:,}"

print(f"El número con formato de pesos es {representacion_valor}")