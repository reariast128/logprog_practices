def get_clients_info(clients_dict):
    return clients_dict.values()

def get_client_debt(client_info):
    return client_info[2]

def get_clients_debt_with_criteria(clients_dict, criteria):
    clients_debt = [get_client_debt(x) for x in get_clients_info(clients_dict)]
    return tuple(filter(criteria, clients_debt))

clientes = {
    'Alicia': (28, 'Chile', 1200),
    'Bob': (45, 'Francia', 2000),
    'Carlos': (30, 'Argentina', 500),
    'David': (23, 'Inglaterra', 0)
}

clients_whit_debt_up_to_1000 = get_clients_debt_with_criteria(clientes, lambda x: x > 1000)
print(clients_whit_debt_up_to_1000)

# Esto es solo una prueba de git
# Otra prueba de git
# Otra prueba de git (otra)