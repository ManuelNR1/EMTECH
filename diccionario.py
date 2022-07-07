diccionario = {
    'llave1' : 1,
    'llave2' : 2,
    'llave3' : 3,
}

población_paises = {
	'Argentina': 44938712,
	'Brasil': 210147125,
	'Colombia': 50372424
}

print(población_paises['Brasil'])

for pais in población_paises.keys():
    print(pais)

for pais in población_paises.values():
    print(pais)

for pais, poblacion in población_paises.items():
    print(pais + ' tiene ' + str(poblacion) + ' habitantes ') 