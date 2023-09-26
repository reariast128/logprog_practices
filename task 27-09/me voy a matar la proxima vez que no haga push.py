def while_element_not_in_list_return_message(element_to_check, list_of_elements, error_message, function_to_do):
    '''Esta función evalúa si element_to_check está en list_of_elements. Si está, no realiza ningún cambio y lo retorna. Si no, ejecuta function_to_do (que debe ser una función que sea de entrada de datos) y vuelve a evaluar, hasta que esté dentro de list_of_elements.'''

    element_to_check = function_to_do()
    while element_to_check not in list_of_elements:
        print(error_message)
        element_to_check = function_to_do()

    return element_to_check

destinies = ('Medellín', 'Bogotá', 'Cartagena')
destinies_abrev = ('MDE', 'BOG', 'CTG')

test = ''
test = while_element_not_in_list_return_message(test, (destinies_abrev + destinies), "Error", lambda: input("Introduce una ciudad: "))

distances = {
    'MDE-BOG': 429,
    'MDE-CTG': 630,
    'BOG-CTG': 1073
}
