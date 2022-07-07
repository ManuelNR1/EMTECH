lista_exportaciones = [3274, 1325, 2254, 533, 6954, 7784, 8414, 7784, 425, 165, 7784, 555]

exportaciones = {'Enero': 3274, 'Febrero': 1325, 'Marzo': 2254, 'Abril': 534, 'Mayo': 6954, 'Junio': 7784, 'Julio': 8414, 'Agosto': 7784, 'Septiembre': 425, 'Octubre': 165, 'Noviembre': 7784}

print(exportaciones['Marzo'])

exportaciones['Diciembre'] = 6555
print(exportaciones,"\n")

del(exportaciones['Enero'])
print(exportaciones,"\n")

exportaciones[2018] = {'Enero': 520,'Febrero': 630,'Marzo': 120}
print(exportaciones,"\n")

print(exportaciones[2018])