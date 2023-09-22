'''
Ejercicio 9

Escriba un programa que permita ingresar tres tipos de productos diferentes (se le 
pide al usuario el nombre), además el usuario ingresa la cantidad y el valor unitario 
de cada producto. El programa debe calcular el valor total de la factura, el IVA y el 
valor antes de IVA. Y deberá imprimir los siguiente:


Producto ------------------------ Cantidad ----------- Valor unitario ----------- Valor total 

CCCCCCCC                            ##                      #####                   ######

DDDDDDDD                            ##                      #####                   ######

EEEEEEEEE                           ##                      #####                   ######

Total antes de IVA                                                                  #######

Total IVA (19%)                                                                     #######

Gran Total                                                                          ######
'''

cant_productos = 3
productos = []
campos_productos = ("Nombre", "Cantidad", "Valor unitario", "Valor total")
subtotal = int()

for i in range(cant_productos):
    valores_producto = []
    print(f"Por favor, introduce la información del producto {i + 1}")
    
    valores_producto.append(input(f"\tIntroduce aquí el valor de '{campos_productos[0]}' -> "))

    cantidad = int(input(f"\tIntroduce aquí el valor de '{campos_productos[1]}' -> "))
    valores_producto.append(cantidad)

    costo = int(input(f"\tIntroduce aquí el valor de '{campos_productos[2]}' -> "))
    valores_producto.append(costo)

    valores_producto.append(cantidad * costo) # Se añade a valores_producto el valor total del producto

    productos.append(dict(zip(campos_productos, valores_producto)))
    subtotal += cantidad * costo

    print("-" * 30, end="\n\n")
    

iva_subtotal = subtotal * .19
total = subtotal + iva_subtotal

print("{:^30}{:^30}{:^30}{:^30}".format(campos_productos[0], campos_productos[1], campos_productos[2], campos_productos[3]))
print("-" * 120)


for producto in productos:
    for valor in producto.values():
        print(f"{valor:^30}", end=" ")
    print("\n")

print("{:^30}{:^30}{:^30}{:^30}".format("Subtotal", "", "", subtotal))
print("{:^30}{:^30}{:^30}{:^30}".format("IVA", "", "", iva_subtotal))
print("{:^30}{:^30}{:^30}{:^30}".format("Total", "", "", total))