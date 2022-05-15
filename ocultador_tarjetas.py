tarjetaint = 1234567890123456

#Convertir el valor de la tarjera a String
tarjeta = str(tarjetaint)

longitud = len(tarjeta)

#Asignar la posicion de inicio del corte
ocultar = longitud - 4

#Empezar el corte del numero de la tarjeta desde la posicion de "ocultar"(12) hasta el final(:)
#Se almacenan los digitos cortados en la variable "numeros_mostrados"
#Al ser "ocultar" una variable, el numero de digitos de la tarjeta puede ser variable
numeros_mostrados = tarjeta[ocultar:]

#imprime asteriscoss igual al numero de numeros que seran ocultados y-
#se concatenan con los numeros que fueron cortados para ser mostrados
print ("*" * ocultar + numeros_mostrados)