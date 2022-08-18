# Parte 1
x = [[5, 2, 3], [10, 8, 9]]
estudiantes = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
directorio_deportes = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

x[1][0] = 15
print(x)

estudiantes[0]['last_name'] = 'Bryant'
print(estudiantes)
directorio_deportes['fútbol'][0] = 'Andres'

z[0]['y'] = 30
print(z)

# Parte 2


def iterateDictionary(dict):
    for i in range(0, len(dict)):
        keys = []
        values = []
        items = dict[i].items()
        for item in items:
            keys.append(item[0]), values.append(item[1])
        print(keys[0], '-', values[0], ',', keys[1], '-', values[1])


estudiantes = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
iterateDictionary(estudiantes)

# Parte 3


def iterateDictionary2(key_name, some_list):
    for i in range(0, len(some_list)):
        print(some_list[i].get(key_name))


iterateDictionary2('first_name', estudiantes)


# Parte 4
def printInfo(some_dict):
    keys = []
    values = []
    items = some_dict.items()
    for item in items:
        keys.append(item[0]), values.append(item[1])
    for i in range(0, len(keys)):
        print(len(values[i]), keys[i])
        for j in range(0, len(values[i])):
            print(values[i][j])


dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)
