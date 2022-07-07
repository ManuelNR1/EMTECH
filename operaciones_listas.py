semestre_1 = [3274, 1325, 2254, 533, 6954, 7784]
semestre_2 = [8414, 7784, 425, 165, 7784, 555]

productos_exportacion = ["Computadoras", "Tablets", "Teclados", "Smartwatch"]

totales = semestre_1 + semestre_2

#print(totales)
#print(totales * 3)

totales[11] = 6555
totales[9] = 2165
#totales[-1] = 6555

print(totales)

print(totales.count(7784))

productos_exportacion.insert(2, 'Audifonos')

# pop remueve tomando el indice como parametro
productos_exportacion.pop(4)
#remove remueve tomando el contenido como parametro
productos_exportacion.remove('Tablets')
print(productos_exportacion)

totales.sort(reverse = True)
#totales.reverse()
print(totales)

elementos = ["Hidrogeno", "Oxigeno", "Azufre", "Calcio"]

elementos.sort( )

print(elementos)