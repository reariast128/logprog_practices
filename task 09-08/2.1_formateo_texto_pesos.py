'''
Ejercicio 2

Escriba un programa al que se le ingrese un valor cualquiera entre 1000 y 999999
y escriba ese mismo número, pero utilizando coma para los miles y signo pesos. Por 
ejemplo, se ingrese 20000 y la salida sea $20,000. 


'''

print("Este programa representa un número en formato de pesos.")
print("Por ejemplo, el número 123456 lo representa como $123,456")
valor = input("Por favor, introduce un valor entre 1000 y 999999 -> ")

representacion_valor = f"${valor[-4::-1][::-1]},{valor[-3:]}"

'''
Explicando esta solución:

Reconozco que es un apaño, y que seguramente haya formas más finas (y sencillas) de conseguir esto mismo.
Supóngase que mi número a trabajar es el 123456.
Aquí lo que uso es el string slicing para acceder a las dos partes que me interesan:
    La que va desde las centenas hasta las unidades (es decir, 456)
    y las que van desde los miles hasta los cientos de miles (es decir, 123)

Dada la condición de que el número debe estar entre 1000 y 999999, se sabe que el número máximo de caracteres que se recibirán son 6.
Por lo tanto, numero las posiciones posibles de estas dos partes del string a trabajar.

| Elementos del string | 1   | 2   | 3   | 4   | 5   | 6   |
| -------------------- | --- | --- | --- | --- | --- | --- |
| Posición (izq a der) |  0  |  1  |  2  |  3  |  4  |  5  |
| Posición (der a izq) | -6  | -5  | -4  | -3  | -2  | -1  |

Para obtener la parte que va desde las centenas hasta las unidades, recorro el string desde -3 hasta 0:
    >>> "123456"[-3:]
        '456'
Para obtener la parte que va desde los miles hasta los cientos de miles, recorro el string desde -4 hasta el final, accediendo con los elementos al revés:
    >>> "123456"[-4::-1]
        '123'

He escogido este método ya que si el número de dígitos dados es mayor o igual a 4 y menor o igual a 6 puedo acceder a los rangos establecidos mediante el slicing.
Si se quisiera soportar números más grandes usando esta solución chapucera, solo se tendían que considerar los caracteres máximos a soportar, dividirlos en grupos de 3, y recorrerlos mediante el slicing.

Gracias por leerse esta biblia profe, es usted un grande.
'''

print(f"El número con formato de pesos es {representacion_valor}")



'''
Solución larga y mucho texto

        representacion_valor = f"${valor[-4::-1][::-1]},{valor[-3:]}"

        
'''