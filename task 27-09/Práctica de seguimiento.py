import random

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

    # Comprobación del pronombre.
    pronoun = None
    pronoun = while_element_not_in_list_return_message(pronoun,
                                                       ('Mr', 'Ms'),
                                                       "\nNo has introducido una opción correcta. Elige entre Mr. o Ms.", 
                                                       lambda: input("\tCómo deseas que nos refiramos a ti? (Mr/Ms): ").capitalize())

    return dict(zip(('name', 'second_name', 'pronoun'), (name, second_name, pronoun)))

def get_user_destiny_from_destinies_list(destinies_list):
    '''Le muestra al usuario los orígenes y destinos desde destinies_list, y le pide al usuario que introduzca la ciudad desde la que va a realizar el vuelo y la ciudad hacia donde realiza el vuelo.
    La función retorna la ciudad de origen del usuario "user_origin" y la ciudad de destino "user_destiny".'''

    print("\nManejamos vuelos entre las siguientes ciudades:")

    for destiny in destinies_list:
        print(f"\t{destiny}")

    user_origin = ''
    user_destiny = ''

    while True:

        # Comprobación del origen.
        user_origin = while_element_not_in_list_return_message(user_origin,
                                                            destinies_list,
                                                            "\nNo has introducido una opción correcta. Elige entre las ciudades disponibles.",
                                                            lambda: input("Por favor, elige la ciudad desde la que tomas el vuelo: ").capitalize())

        # Comprobación del destino.
        user_destiny = while_element_not_in_list_return_message(user_destiny,
                                                            destinies_list,
                                                            "\nNo has introducido una opción correcta. Elige entre los destinos disponibles.",
                                                            lambda: input("Por favor, elige un destino: ").capitalize())

        # Comprobación de que el origen no sea igual al destino.
        if user_origin != user_destiny:
            break
        else:
            print("Has digitado la misma opción para ciudad de origen y ciudad de destino. Por favor, digita opciones distintas.")
            print("-" * 30)
            print()

    return user_origin, user_destiny

def get_user_flight_return_date():
    '''Esta función le pregunta al usuario el día de mes de salida "flight_date" y "return_date" y valida que esté entre 1 y 30, y el día de la semana "week_day",  y valida que esté entre "Lunes" y "Domingo".
    Retorna "flight_date", "return_date", y "week_day".'''

    days_of_month = [x for x in range(1, 31)]
    days_of_week = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    flight_date = 0
    return_date = 0
    week_day = ''

    while True:

        # Asignación y validación del día de partida
        flight_date = int(while_element_not_in_list_return_message(flight_date, 
                                                                   days_of_month,
                                                                   "No has ingresado una opción válida. Por favor, vuelve a escribir la fecha.", 
                                                                   lambda: int(input("\nAhora, introduce la fecha a la que vas a viajar (por ejemplo, 9): "))))
        
        # Asignación y validación del día de retorno.
        return_date = int(while_element_not_in_list_return_message(return_date,
                                                                   days_of_month,
                                                                   "No has ingresado una opción válida. Por favor, vuelve a escribir la fecha.",
                                                                   lambda: int(input("\nAhora, introduce la decha a la que vas a regresar (por ejemplo, 11): "))))

        # Validación de que la fecha de retorno no sea menor a la de partida.
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

def get_flight_distance(origin, destiny, distances_dict):
    '''Esta función obtiene la distancia entre "origin" y "destiny", buscando si existen en las llaves del diccionario distances_dict.
    Retorna el valor de "distances_dict[(origin, destiny)], que corresponde a la distancia entre la ciudad de origen y destino.'''

    if (origin, destiny) in distances_dict:
        return distances[(origin, destiny)]
    else:
        print(f"Error: No existe el valor de la distancia para estos destinos: {origin}, {destiny}")

def get_flight_price(distance, flight_date):

    '''Esta función retorna un precio de vuelo en relación a la distancia entre las ciudades y el día de la semana en la que se haga el viaje.
    Las pautas para los condicionales se hicieron conforme a lo expuesto en el archivo de práctica.'''

    days_of_week = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

    if flight_date in days_of_week[0:4]:
        if distance < 400:
            return 779000
        else:
            return 156900
    elif flight_date in days_of_week[4:7]:
        if distance < 400:
            return 119900
        else:
            return 213000

def get_user_chair():

    '''Esta función le pregunta al usuario qué opción de asiento desea.
    Retorna el caracter de la opción ("A", "B", "C") concatenado a un número aleatorio entre 1 y 29.'''

    print("Tenemos las siguientes opciones para que escojas el asiento:")
    print("\tAl lado de la ventana (opción 'A')")
    print("\tTe es indiferente (opción 'B')")
    print("\tAl lado del pasillo (opción 'C')")

    chair_type = None
    chair_type = while_element_not_in_list_return_message(chair_type,
                                                         ('A', 'B', 'C'),
                                                         "No has ingresado una opción de asiento válida",
                                                         lambda: input("\nPor favor, elige entre una de las opciones anteriores: ")
    )

    return chair_type + str(random.randint(1, 29))

if __name__ == '__main__':

    reservation_list = []

    while True:

        # Mensaje de bienvenida.
        print("\nBienvenidx al programa de reserva de vuelos. Por favor, indícanos la siguiente información:")
        user_info = get_user_info()
        print(f"{user_info['pronoun']}. {user_info['name']} {user_info['second_name']}, bienvenidx a la aerolínea FastFast")


        # Definición de los destinos disponibles y sus distancias.
        destinies = ('Medellín', 'Bogotá', 'Cartagena')
        distances = {
            ('Medellín', 'Bogotá'): 416, 
            ('Medellín', 'Cartagena'): 639,
            ('Bogotá', 'Cartagena'): 1037
        }

        # Obtención del origen y destino del usuario.
        user_origin, user_destiny = get_user_destiny_from_destinies_list(destinies)

        # Obtención de las fechas en las que el usuario sale y regresa.
        user_flight_date, user_return_date, user_week_day = get_user_flight_return_date()

        # Obtención de la distancia entre ciudades de origen y de destino.
        user_flight_distance = get_flight_distance(user_origin, user_destiny, distances)

        # Obtención del precio del boleto en relación a la distancia entre ciudades.
        user_fligt_price = get_flight_price(user_flight_distance, user_week_day)

        # Obtención de la silla 
        user_chair = get_user_chair()

        # Añadir el diccionario con la información del usuario a la lista de reservas.
        reservation_list.append({
            user_chair: (user_info['name'], user_destiny, user_fligt_price)
        })

        add_user = None
        add_user = while_element_not_in_list_return_message(add_user,
                                                            ('S', 'N'),
                                                            "No has ingresado una opción correcta.",
                                                            lambda: input("\nDeseas añadir más usuarios? (S/N): ").upper()
        )

        if add_user == 'N':
            break
        else:
            continue

    for reservation in reservation_list:
        print(reservation)