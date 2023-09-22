'''
Ejercicio 5

Escriba un programa que calcule cuánto debe sacar un estudiante de cálculo 
diferencial en el examen final para aprobar con 3.0. Si el usuario ingresa la nota del 
parcial 1 (20%), la nota del parcial 2 (25%), el seguimiento (25%) y el examen final 
tiene un valor del 30% (Se admiten valores negativos como respuesta).
'''

valor_parcial1 = .2
valor_parcial2 = .25
valor_seguimiento = .25
valor_examen_final = .3

print("Este programa calcula cuánto tienes que sacar en el examen final de cálculo diferencial para aprobar la materia con 3.0, teniendo en cuenta que:")
print(f"\tEl primer parcial vale {valor_parcial1:%}")

print(f"\tEl segundo parcial vale {valor_parcial2:%}")
print(f"\tEl seguimiento vale {valor_seguimiento:%}")
print(f"\tEl examen final vale {valor_examen_final:%}")

print("\n A continuación, vas a introducir las notas separando los decimales con puntos. Por ejemplo, '3.2'\n")

nota_parcial1 = float(input("Introduce la nota que sacaste en el primer parcial: "))
nota_parcial2 = float(input("Introduce la nota que sacaste en el segundo parcial: "))
nota_seguimiento = float(input("Introduce la nota que sacaste en el seguimiento: "))

nota_corte = nota_parcial1 * valor_parcial1 + nota_parcial2 * valor_parcial2 + nota_seguimiento * valor_seguimiento
nota_requerida_examen_final = round((3 - nota_corte) / valor_examen_final, 3)

print(f"\nPara aprobar la materia con 3.0, necesitas sacar en el examen final {nota_requerida_examen_final}")