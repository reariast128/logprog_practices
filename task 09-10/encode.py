def text_to_number_list(text):
    return [ord(letter) for letter in text]


def encode_message(message, key = 0):
    return ''.join(list(map(lambda letter_number: chr(letter_number + key), text_to_number_list(message))))

def decode_message(encoded_message, key):
    return ''.join(list(map(lambda letter_number: chr(letter_number - key), text_to_number_list(encoded_message))))

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