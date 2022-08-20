import csv
direccion = "synergy_logistics_database.csv"

def top10_rutas():
    lista_origenes = []
    lista_destinos = []
    rutas = []
    viajes_rutas = {}
    dict_viajes_ordenado = {}

    with open(direccion, mode="r") as archivo_csv:
        registros = csv.DictReader(archivo_csv)
        for registro in registros:
            if registro["origin"] not in lista_origenes:
                lista_origenes.append(registro["origin"])
            if registro["destination"] not in lista_destinos:
                lista_destinos.append(registro["destination"])
        #crear lista de rutas, donde cada ruta es una tupla (origen, destino)
        for destino in lista_destinos:
            for origen in lista_origenes:
                if destino == origen:
                    continue
                rutas.append((origen,destino))
        numero_rutas = len(rutas)
        #crear el diccionario de rutas con el numero de viajes como valor a partir de la lista de rutas
        for route in rutas:
            viajes_rutas[route] = 0

    #Evaluar la cantidad de veces que se llevó a cabo una ruta
    with open(direccion, mode="r") as archivo2_csv:
        filas = csv.DictReader(archivo2_csv)
        for fila in filas:
            for ruta in viajes_rutas:
                if ruta[0] == fila["origin"] and ruta[1] == fila["destination"]:
                    viajes_rutas[ruta] += 1
        #Crear dict ordenado con base a los valores mas altos del diccionario viajes_rutas
        valores_ordenados = sorted(viajes_rutas.values(), reverse= True)
        for i in valores_ordenados:
            for k in viajes_rutas.keys():
                if viajes_rutas[k] == i:
                    dict_viajes_ordenado[k] = viajes_rutas[k]
                    break
        i=0
        print("\nLas 10 rutas más demandadas son:")
        for ruta in dict_viajes_ordenado:
            print(i+1,list(ruta), "con:", dict_viajes_ordenado[ruta], "viajes")
            i+=1
            if i == 10:
                break

def top3_transportes():
    lista_transportes = []
    lista_valores = []
    dict_transportes = {}
    dict_transportes_ordenado = {}

    with open(direccion, mode="r") as archivo_csv:
            registros = csv.DictReader(archivo_csv)
            for registro in registros:
                if registro["transport_mode"] not in lista_transportes:
                    lista_transportes.append(registro["transport_mode"])
                lista_valores.append(int(registro["total_value"]))
            for transporte in lista_transportes:
                dict_transportes[transporte] = 0

    with open(direccion, mode="r") as archivo2_csv:
            filas = csv.DictReader(archivo2_csv)
            for fila in filas:
                for transporte in lista_transportes:
                    if transporte == fila["transport_mode"]:
                        dict_transportes[transporte] += int(fila["total_value"])
            
            valores_ordenados = sorted(dict_transportes.values(), reverse= True)
            for i in valores_ordenados:
                for k in dict_transportes.keys():
                    if dict_transportes[k] == i:
                        dict_transportes_ordenado[k] = dict_transportes[k]
                        break
            
            i=0
            print("\nLos 3 medios de transporte más relevantes considerando los valores de importación y exportación son:")
            for key,value in dict_transportes_ordenado.items():
                print(i+1, "-", key, "con un total de:", value)
                i+=1
                if i == 3:
                    break

def top80paises():
    lista_origenes = []
    lista_valores = []
    dict_paises = {}
    paises_vip = []
    dict_paises_ordenado = {}
    valor_total = 0
    valor_80 = 0

    with open(direccion, mode="r") as archivo_csv:
            registros = csv.DictReader(archivo_csv)
            for registro in registros:
                if registro["origin"] not in lista_origenes:
                    lista_origenes.append(registro["origin"])
                lista_valores.append(int(registro["total_value"]))
                valor_total = sum(lista_valores)
                valor_80 = valor_total * 0.80

            for origen in lista_origenes:
                    dict_paises[origen] = 0

    with open(direccion, mode="r") as archivo2_csv:
            filas = csv.DictReader(archivo2_csv)
            for fila in filas:
                for origen in lista_origenes:
                    if origen == fila["origin"]:
                        dict_paises[origen] += int(fila["total_value"])
            
            valores_ordenados = sorted(dict_paises.values(), reverse= True)
            for i in valores_ordenados:
                for k in dict_paises.keys():
                    if dict_paises[k] == i:
                        dict_paises_ordenado[k] = dict_paises[k]
                        break
            
            p = 0
            for key in dict_paises_ordenado:
                p += dict_paises_ordenado[key]
                paises_vip.append((key,dict_paises_ordenado[key]))
                if p >= valor_80:
                    break
            
            print("\nLos paises que generan el 80%","del valor de las exporaciones e importaciones son:") 
            i=0
            for pais, valor in paises_vip:
                print(i+1, "-", pais, "con un valor de:",valor)
                i+=1

nombre_de_usuario = "emtech"
contraseña = "caso2"
login_usuario = input("Ingresa usuario: ")
login_contraseña = input("Ingresa contraseña: ")

login = login_usuario == nombre_de_usuario and login_contraseña == contraseña
if login:
    top10_rutas()
    top3_transportes()
    top80paises()
else:
    print("Intenta de nuevo")