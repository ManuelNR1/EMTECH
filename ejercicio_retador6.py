from operator import itemgetter

#Lista que contendrá los detalles ingresados por el pasajero
pasajeros = []

#Listas que son requeridas en el output del programa
detalles_vuelos = []
edades_promedios = []

#Variables de edades y numero de viajes por destino
edades_bjx = 0
edades_gdl = 0
edades_jal = 0

viajes_bjx = 0
viajes_gdl = 0
viajes_jal = 0

#Input cíclico donde se evalúa que el nombre sea distinto de X
while 1 == 1:
    nombre = input("Nombre: ")
    if nombre == "X" or nombre == "x":
        break
    edad = int(input("Edad: "))
    destino = input("IATA del Destino: ")
    while destino != 'GDL' and destino != 'BJX' and destino != 'JAL':
            destino = input('IATA del destino no válida, ingresar nueva IATA: ')
    pasajeros.append((nombre, edad, destino))

#Recorrer la lista pasajeros para calcular el numero de viajes y edad total por destino
for pasajero in pasajeros:
    if pasajero[2] == "BJX":
        viajes_bjx += 1
        edades_bjx += pasajero[1]
    elif pasajero[2] == "GDL":
        viajes_gdl += 1
        edades_gdl += pasajero[1]
    elif pasajero[2] == "JAL":
        viajes_jal += 1
        edades_jal += pasajero[1]

#Calcular el promedio de edades por destino
#Se crea un excepción cuando se divide entre 0
try:
    edad_promedio_bjx = edades_bjx / viajes_bjx
except ZeroDivisionError:
    edad_promedio_bjx = 0
try:
    edad_promedio_gdl = edades_gdl / viajes_gdl
except ZeroDivisionError:
    edad_promedio_gdl = 0
try:
    edad_promedio_jal = edades_jal / viajes_jal
except ZeroDivisionError:
    edad_promedio_jal = 0

#Llenar las listas solicitadas
detalles_vuelos.append(("BJX", viajes_bjx))
detalles_vuelos.append(("GDL", viajes_gdl))
detalles_vuelos.append(("JAL", viajes_jal))

edades_promedios.append(("BJX", edad_promedio_bjx))
edades_promedios.append(("GDL", edad_promedio_gdl))
edades_promedios.append(("JAL", edad_promedio_jal))

#Ordena las listas con base a la posicion 1 de las tuplas (numero de viajes o edades promedio)
#Se ordenan en reversa para que vayan de mayor a menor
print("Detalles de vuelos:")
print(sorted(detalles_vuelos, key=itemgetter(1), reverse=True))
print("Edad promedio por vuelo:")
print(sorted(edades_promedios, key=itemgetter(1), reverse=True))