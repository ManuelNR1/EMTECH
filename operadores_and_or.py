edad_cliente = int(input('Ingresa tu edad: '))
tarjeta_credito = edad_cliente >= 18 and edad_cliente <=70
print("Puedes tener tarjeta de credito:", tarjeta_credito)

descuento = edad_cliente == 20 or edad_cliente == 30
print("Puedes obtener el descuento:", descuento)

cadena = input("Ingresa una palabra: ")
resultado_cadena = len(cadena)>5 and cadena[2] == "h"
print("Palabra ganadora:", resultado_cadena)