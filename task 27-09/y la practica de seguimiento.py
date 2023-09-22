def while_element_not_in_list_return_message(element_to_check, list_of_elements, error_message, function_to_do):
    '''Esta función evalúa si element_to_check está en list_of_elements. Si está, no realiza ningún cambio y lo retorna. Si no, ejecuta function_to_do (que debe ser una función que sea de entrada de datos) y vuelve a evaluar, hasta que esté dentro de list_of_elements.'''

    while element_to_check not in list_of_elements:
        print(error_message)
        element_to_check = function_to_do()

    return element_to_check

def get_user_info():
    '''Retorma un diccionario de esta forma:
        {
            'name': name,
            'second_name': second_name,
            'pronoun': pronoun
        }
    '''
    name = input("\tIntroduce tu nombre: ")
    second_name = input("\tIntroduce tu apellido: ")
    pronoun = input("\tCómo deseas que nos refiramos a ti? (Mr/Ms): ").capitalize()

    # Comprobación del pronombre
    pronoun = while_element_not_in_list_return_message(pronoun, 
                                                       ('Mr', 'Ms'), 
                                                       "\nNo has introducido una opción correcta. Elige entre Mr. o Ms.", 
                                                       lambda: input("\tCómo deseas que nos refiramos a ti? (Mr/Ms): ").capitalize())

    return dict(zip(('name', 'second_name', 'pronoun'), (name, second_name, pronoun)))

def get_user_destiny_from_destinies_list(destinies_list):
    print("\nManejamos vuelos entre las siguientes ciudades:")

    for destiny in destinies_list:
        print(f"\t{destiny}")

    user_origin = ''
    user_destiny = ''

    while True:        
        user_origin = input("Por favor, elige la ciudad desde la que tomas el vuelo: ").capitalize()

        # Comprobación del origen
        user_origin = while_element_not_in_list_return_message(user_origin,
                                                            destinies_list,
                                                            "\nNo has introducido una opción correcta. Elige entre las ciudades disponibles.",
                                                            lambda: input("Por favor, elige la ciudad desde la que tomas el vuelo: ").capitalize())

        user_destiny = input("Por favor, elige un destino: ").capitalize()

        # Comprobación del destino
        user_destiny = while_element_not_in_list_return_message(user_destiny,
                                                            destinies_list,
                                                            "\nNo has introducido una opción correcta. Elige entre los destinos disponibles.",
                                                            lambda: input("Por favor, elige un destino: ").capitalize())

        # Comprobación de que el origen no sea igual al destino
        if user_origin != user_destiny:
            break
        else:
            print("Has digitado la misma opción para ciudad de origen y ciudad de destino. Por favor, digita opciones distintas.")
            print("-" * 30)
            print()

    return user_origin, user_destiny

# Mensaje de bienvenida
print("\nBienvenidx al programa de reserva de vuelos. Por favor, indícanos la siguiente información:")
user_info = get_user_info()
print(f"{user_info['pronoun']}. {user_info['name']} {user_info['second_name']}, bienvenidx a la aerolínea FastFast")


# Definición del destino
destinies = ('Medellín', 'Bogotá', 'Cartagena')
user_destiny = get_user_destiny_from_destinies_list(destinies)
print(user_destiny)
