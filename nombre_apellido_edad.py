nombre_edad = input("Ingresa Un nombre, apellido y edad: ")

x = nombre_edad.find(" ")

nombre = nombre_edad[0:x]

y = nombre_edad.find(" ", x+1)

apellido = nombre_edad[x+1:y]

edad = int(nombre_edad[y+1:])

edad_futura = edad + 25

print("El nombre es {name}, se apellida {lastname} y en 25 años va a tener {años}".format(name = nombre, lastname = apellido, años = edad_futura))

