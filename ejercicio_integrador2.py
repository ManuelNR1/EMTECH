import csv
numero_pasajeros = []
tuplas_pasajeros = []
top5 = []
topmin5 = []
promedio_min_max = []

def lectura(direccion):
    with open(direccion, mode="r") as archivo_csv:
     registros = csv.DictReader(archivo_csv)
     for registro in registros:
        if registro["Pasajeros"] == "Pasajeros" or registro["Ciudad"]=="Ciudad":
            continue
        tuplas_pasajeros.append((registro["Ciudad"] ,int(registro["Pasajeros"])))
        numero_pasajeros.append(int(registro["Pasajeros"]))

#Promedio de pasajeros de todos los aeropuertos
def promedioPasajeros():     
    print("\n-El promedio total de pasajeros es de:", round(sum(numero_pasajeros)/len(numero_pasajeros),1),"\n")

#Los 5 aeropuertos con mayor cantidad de Pasajeros
def mayorPasajeros():
    lista_ordenada = sorted(tuplas_pasajeros, key= lambda x: x[1], reverse = True)
    #print(lista_ordenada)
    i = 0
    while i < 5:
        top5.append(lista_ordenada[i])
        i += 1
    print("-Los 5 aeropuertos con mayor cantidad de pasajeros son:\n", top5)
    
#Los 5 aeropuertos con menos pasajeros
def menosVuelosSin():
    lista_ordenada_min = sorted(tuplas_pasajeros, key= lambda x: x[1])
    #print(lista_ordenada_min)
    j = 0
    for aero in lista_ordenada_min:
        if aero[1] == 0:
            continue
        topmin5.append(aero)
        j += 1
        if j == 5:
            break
    print("-Los 5 aeropuertos con menor cantidad de vuelos a Sinaloa son:\n", topmin5,"\n")

#Escribir en CSV los resultados de mayorPasajeros() y menosVuelosSin()
def escritorCSV():
    with open("info_1_3.csv", "w") as archivo:
        campos = ["Aeropuertos con mas pasajeros:"]
        campos1 = ["Aeropuertos con menos vuelos a Sinaloa:"]

        escritor = csv.writer(archivo)
        
        escritor.writerow(campos)
        escritor.writerows(top5)
        escritor.writerow(campos1)
        escritor.writerows(topmin5)

#Promedio de pasajeros de mayorPasajeros() y menosVuelosSin()
def promedioMaxMin():
    promedio = top5 + topmin5
    for fila in promedio:
        promedio_min_max.append(fila[1])
    print("-El promedio total de pasajeros es de ambos aeropuertos es:", round(sum(promedio_min_max)/len(promedio_min_max),1),"\n")

lectura("Ejercicio Integrador 2.csv")
mayorPasajeros()
promedioPasajeros()
menosVuelosSin()
escritorCSV()
promedioMaxMin()