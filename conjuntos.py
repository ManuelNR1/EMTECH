paises = ['México', 'Honduras', 'Brasil', 'Honduras', 'Jamaica', 'México', 'Colombia', 'Nicaragua', 'Panamá', 'Paraguay', 'Brasil', 'Argentina', 'México', 'Brasil', 'Chile', 'Colombia', 'Panamá', 'Perú', 'Argentina', 'Uruguay']

print(len(paises))

conjunto_paises = set(paises)
print(conjunto_paises)
print(len(conjunto_paises))

conjunto_exportaciones = {874, 4829, 3402, 324, 420, 420}
print(conjunto_exportaciones)

conjunto_paises.add('Ecuador')
#print(conjunto_paises)

#El elemento se elimina aleatoriamente
conjunto_paises.pop()
#print(conjunto_paises)

#Eliminar de manera selectiva
conjunto_paises.remove('Brasil')
#print(conjunto_paises)

top_paises = {'México', 'Colombia', 'Argentina', 'Costa Rica'}
diferencia = conjunto_paises.difference(top_paises)
#Muestra los paises que no estan en la lista del top 4
print(diferencia)

interseccion = conjunto_paises.intersection(top_paises)
#Muestra los paises que hay en ambos conjuntos a la vez
print(interseccion)

union = conjunto_paises.union(top_paises)
#Suma los 2 conjuntos
print(union)