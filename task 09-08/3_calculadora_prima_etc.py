'''
Ejercicio 3

Escriba un programa que dado un sueldo mensual y una cantidad de días laborados 
calcule: la prima de servicios, las cesantías, las vacaciones, los intereses a las 
cesantías y el total de liquidación (suma de los anteriores valores). 
'''

print("Este programa calcula a prima de servicios, las cesantías, las vacaciones, los intereses a las cesantías y el total de liquidación")

sueldo_mensual = float(input("Por favor, introduce tu sueldo mensual (sin incluir el subsidio de transporte)-> "))
dias_trabajados = float(input("Por favor, introduce los días trabajados este semestre -> "))

subsidio_transporte = 140606

prima = round((sueldo_mensual + subsidio_transporte) * dias_trabajados / 360) #fuente: https://www.larepublica.co/finanzas/como-se-calcula-la-prima-de-mitad-de-ano-3628225
cesantias = round(((sueldo_mensual + subsidio_transporte) * dias_trabajados * 2) / 360)
intereses_cesantias = round((cesantias * .12 * dias_trabajados * 2) / 360)
vacaciones = round((sueldo_mensual * dias_trabajados * 2) / 720)

total_liquidacion = prima + cesantias + intereses_cesantias + vacaciones

print("Estos son los valores calculados:")
print(f"\tLa prima es de {prima}")
print(f"\tLas cesantías son de {cesantias}")
print(f"\t Los intereses de las cesantías son de {intereses_cesantias}")
print(f"\tLas vacaciones son de {vacaciones}")
print(f"El total de la liquidación es de {total_liquidacion}")