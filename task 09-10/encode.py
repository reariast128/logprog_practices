'''
Las funciones de este programa trabajan con strings codificados en unicode.
'''

def text_to_number_list(text):
    '''Esta función crea una lista con los códigos de loscaracteres de text.'''

    return [ord(letter) for letter in text]

def encode_message(message, key = 0):
    '''Esta función desplaza cada índice de caracter del mensaje en key unidades, y retorna un string con los caracteres con índices desplazados.
    Nótese que si key > 0, los índices de caracter se desplazan a la izquierda.'''

    return ''.join(list(map(lambda letter_number: chr(letter_number + key), text_to_number_list(message))))

def decode_message(encoded_message, key):
    '''Esta función desplaza cada caracter del mensaje en -key unidades, y retorna un string con los caracteres desplazados.
    Nótese que si key > 0, los índices de caracter se desplazan a la derecha.'''
    
    return ''.join(list(map(lambda letter_number: chr(letter_number - key), text_to_number_list(encoded_message))))

if __name__ == '__main__':
    message = input("Introduce el mensaje: ")
    key = None

    while True:
        try:
            key = int(input("Introduce la cantidad de letras a desplazar (la llave): "))
            break
        except:
            print("No has ingresado una opción válida.\n")

    encoded_message = encode_message(message, key)
    decoded_message = decode_message(encoded_message, key)

    print(encoded_message)
    print(decoded_message)