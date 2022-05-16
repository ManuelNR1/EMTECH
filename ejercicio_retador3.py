capacidad_maxima = 3254
capacidad_minima = capacidad_maxima / 2

peso_cemento_kg = 40
peso_yeso_kg = 30

costales_cemento = int(input("Ingresa costales de cemento: "))
costales_yeso = int(input("Ingresa costales de yeso: "))

peso_total_cemento = peso_cemento_kg * costales_cemento
peso_total_yeso = peso_yeso_kg * costales_yeso
peso_total = peso_total_cemento + peso_total_yeso
print("Su peso total en kg es:", peso_total)

estado_envio = peso_total >= capacidad_minima and peso_total <= capacidad_maxima
print("¿Se puede realizar el envio?:", estado_envio)