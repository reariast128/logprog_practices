import random

while True:
    print("Este programa es un juego. El programa genera un número aleatorio entre 1 y 10, y tú tendrás que adivinarlo.")

    rand_num = random.randint(1, 10)
    user_tryes = 3

    print(rand_num)

    while True:
        user_num = int(input("Introduce un número del uno al 10: "))
        user_num_is_bigger = user_num > rand_num

        user_tryes -= 1
        
        if user_num == rand_num:
            print(f"Acertaste! El número correcto es {rand_num}")
            break

        print(f"{'El número que ingresaste es mayor al generado.' if user_num_is_bigger else 'El número que ingresaste es mayor al generado.'}")
        

        if user_tryes == 0:
            print(f"Perdiste! El número correcto era {rand_num}.")
            break
    
    print("-"*30, "\n")

    while True:
        seguir_jugando = input("Deseas seguir jugando? (s/n): ").lower()
        
        match seguir_jugando:
            case 's':
                break
            case 'n':
                print("Gracias por jugar!")
                exit()
            case _:
                print("No has ingresado una opción correcta.\n")
