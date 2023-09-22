'''
Ejercicio 8

Escriba un programa que al ingresar un valor de tiempo en segundos, calcule la 
cantidad en minutos, horas, días y meses. 
'''

print("Este programa recibe un valor de tiempo en segundos, y lo muestra en minutos, horas, dias y meses.")
tiempo = int(input("Introduce el valor -> "))

tiempo_minutos = tiempo / 60
tiempo_horas = tiempo_minutos / 60
tiempo_dias = tiempo_horas / 24
tiempo_meses = tiempo_dias / 30

print(f"El valor que ingresaste en minutos es de {tiempo_minutos}")
print(f"El valor que ingresaste en horas es de {tiempo_horas}")
print(f"El valor que ingresaste en días es de {tiempo_dias}")
print(f"El valor que ingresaste en meses es de {tiempo_meses}")

'''
Solución 2

Creo que igual se debería empezar por meses y de ahí ir sacando los acarreos y esa monda
'''

