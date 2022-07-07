exp2019 = [3274, 1325, 2254, 533, 6954, 7784, 8414, 7784, 425, 165, 7784, 6555]

numero_exportaciones = len(exp2019)

print(numero_exportaciones)

total_exportaciones = sum(exp2019)

promedio_exp2019 =  total_exportaciones / numero_exportaciones
print('El promedio de exportaciones realizadas en 2019 es: ', promedio_exp2019)

exportaciones = {'Enero': 3274, 'Febrero': 1325, 'Marzo': 2254,
 'Abril': 534, 'Mayo': 6954, 'Junio': 7784, 'Julio': 8414,
 'Agosto': 7784, 'Septiembre': 425, 'Octubre': 165,
 'Noviembre': 7784}

longitud = len(exportaciones)
suma = sum(exportaciones.values())

print(exportaciones.values())
print(suma / longitud)



numeros = [2, 3, 5]

print(sum(numeros)*3)