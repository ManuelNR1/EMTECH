import csv

rutas = {}
lista_paises = []
lista_destinos = []

direccion = "synergy_logistics_database.csv"

with open(direccion, mode="r") as archivo_csv:
    registros = csv.DictReader(archivo_csv)
    for registro in registros:
        if registro["destination"] not in lista_destinos:
            lista_destinos.append(registro["destination"])
        rutas[registro["origin"]] = lista_destinos
    print(len(lista_destinos))
    print(rutas)