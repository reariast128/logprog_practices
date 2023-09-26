def reversed_range_list(max_number):
    return [x for x in reversed(range(1, max_number + 1))]

lista = ['Alicia', 3]
print(lista)

print(f"La lista actual tiene los siguientes elementos: {lista}")
user_number = int(input("Introduce un número: "))
if user_number > 0:
    list_from_user_number = reversed_range_list(user_number)
    for number in list_from_user_number:
        lista.append(number)
    print(f"La nueva lista tiene los siguientes elementos: {lista}")

else:
    print("Estoy programado para no hacer nada si el número es menor o igual a cero.")