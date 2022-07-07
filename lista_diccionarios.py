exp2019 = {'Enero': 3274,'Febrero': 1325,'Marzo': 2254}
exp2018 = {'Enero': 210,'Febrero': 610,'Marzo': 120}
exp2017 = {'Enero': 420,'Febrero': 223,'Marzo': 985}
exp2016 = {'Enero': 590,'Febrero': 3432,'Marzo': 763}


#exportaciones = []

#exportaciones.append(exp2019)
#exportaciones.append(exp2018)
#exportaciones.append(exp2017)
#exportaciones.append(exp2016)

#print(exportaciones)

exportaciones = [
    {'Enero': 3274,'Febrero': 1325,'Marzo': 2254}, 
    {'Enero': 210,'Febrero': 610,'Marzo': 120}, 
    {'Enero': 420,'Febrero': 223,'Marzo': 985}, 
    {'Enero': 590,'Febrero': 3432,'Marzo': 763}
]

print(exportaciones[0])
print(exportaciones[1]['Marzo'])

#Convertir una lista a diccionario
datos = [('Enero', 650), ('Febrero', 420), ('Marzo', 510)]

datos_meses = dict(datos)
print(datos_meses)