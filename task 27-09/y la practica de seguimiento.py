def while_element_not_in_list_return_message(element_to_check, list_of_elements, error_message, function_to_do):
    '''Esta función ejecuta function_to_do y evalúa si element_to_check está en list_of_elements. Si está, no realiza ningún cambio y lo retorna. Si no, ejecuta function_to_do (que debe ser una función que sea de entrada de datos) y vuelve a evaluar, hasta que esté dentro de list_of_elements.'''
    
    element_to_check = function_to_do()
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

    # Comprobación del pronombre
    pronoun = None
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

        # Comprobación del origen
        user_origin = while_element_not_in_list_return_message(user_origin,
                                                            destinies_list,
                                                            "\nNo has introducido una opción correcta. Elige entre las ciudades disponibles.",
                                                            lambda: input("Por favor, elige la ciudad desde la que tomas el vuelo: ").capitalize())

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

def get_user_flight_return_date():

    days_of_month = [x for x in range(1, 31)]
    days_of_week = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    flight_date = 0
    return_date = 0
    week_day = ''

    while True:

        flight_date = int(while_element_not_in_list_return_message(flight_date, 
                                                                   days_of_month,
                                                                   "No has ingresado una opción válida. Por favor, vuelve a escribir la fecha.", 
                                                                   lambda: int(input("\nAhora, introduce la fecha a la que vas a viajar (por ejemplo, 9): "))))
        
        return_date = int(while_element_not_in_list_return_message(return_date,
                                                                   days_of_month,
                                                                   "No has ingresado una opción válida. Por favor, vuelve a escribir la fecha.",
                                                                   lambda: int(input("\nAhora, introduce la decha a la que vas a regresar (por ejemplo, 11): "))))

        if return_date < flight_date:
            print("No has ingresado una opción válida. Por favor, vuelve a escribir la información.")
            print("-" * 30)
            print()
            continue
        else:
            week_day = while_element_not_in_list_return_message(week_day,
                                                            days_of_week,
                                                            "No has ingresado una opción válida. Por favor, vuelve a escribir el día de la semana.",
                                                            lambda: input("Qué día de la semana vas a viajar? (por ejemplo, miércoles): "))
            break

    return flight_date, return_date, week_day

def get_user_flight_price(origin, destiny, flight_date, distances_dict):
    pass

# Mensaje de bienvenida
print("\nBienvenidx al programa de reserva de vuelos. Por favor, indícanos la siguiente información:")
user_info = get_user_info()
print(f"{user_info['pronoun']}. {user_info['name']} {user_info['second_name']}, bienvenidx a la aerolínea FastFast")


# Definición del destino
destinies = ('Medellín', 'Bogotá', 'Cartagena')
distances = {
    ('Medellín', 'Bogotá'): 416, 
    ('Medellín', 'Cartagena'): 639,
    ('Bogotá', 'Cartagena'): 1037
}
user_origin, user_destiny = get_user_destiny_from_destinies_list(destinies)
user_flight_date, user_return_date, user_week_day = get_user_flight_return_date()
user_fligt_price = get_user_flight_price(distances)