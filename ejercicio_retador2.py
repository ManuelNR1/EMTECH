import statistics

i = 3
municipios = []
habitantes = []

while i > 0:
    municipio_nuevo = input("Ingrese municipio: ")
    municipios.append(municipio_nuevo)

    habitantes_nuevo = int(input("Ingresar número de hábitantes: "))
    habitantes.append(habitantes_nuevo)

    i -= 1

total_habitantes = sum(habitantes)
print("Total de habitantes: ", total_habitantes)

promedio_habitantes = float(statistics.mean(habitantes))
print("Promedio de habitantes: ", promedio_habitantes)