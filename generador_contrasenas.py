import random

def generar_contraseña():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    simbolos = ['!', '#', '$', '%', '&', '/', '(', ')', '=', '+', '-', '*', '?', '¿', '¡']
    numeros = ['1','2','3','4','5','6','7','8','9','0']

    caracteres = mayusculas + minusculas + simbolos + numeros
    contraseña = []

    for i in range (15):
        caracter_random = random.choice(caracteres)
        contraseña.append(caracter_random)
# Convierte la lista en un string
    contraseña = "".join(contraseña)
    return contraseña

contraseña = generar_contraseña()
print("\nTu nueva contraseña es: " + contraseña + '\n')