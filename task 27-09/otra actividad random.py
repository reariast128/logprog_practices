def count_amount_of_friends(friends_dict):
    amount_of_friends = [len(x) for x in friends_dict.values()]
    return dict(zip(friends_dict.keys(), amount_of_friends))
    

amigos = {
    'Bob': ['Patricio', 'Calamardo', 'Arenita', 'Don Cangrejo'],
    'Patricio': ['Bob', 'Calamardo'],
    'Arenita': ['Bob'],
    'Calamardo': [],
    'Don Cangrejo': ['Bob', 'Calamardo']
}

print(count_amount_of_friends(amigos))