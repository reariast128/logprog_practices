'''
Notas:
    No voy a considerar las letras con acentos, ni puntos, ni Ñ o ñ por el momento. Otro día quizás.
'''

unicode_codes = {
    'punctuation1': [code for code in range(32, 47)],
    'digits': [code for code in range(48, 57)],
    'punctuation2': [58, 64],
    'upper_a_to_z': [code for code in range(65, 90)],
    'lower_a_to_z': [code for code in range(97, 122)]
}

def text_to_number_list(text):
    return [ord(letter) for letter in text]


def encode_number_list(number_list, key):
    pass

message = input("Introduce el mensaje: ")

'''while True:
    try:
        key = int(input("Introduce la cantidad de letras a desplazar (la llave): "))
        break
    except:
        print("No has ingresado una opción válida.\n")'''

print(text_to_number_list(message))