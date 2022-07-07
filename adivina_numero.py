import random

numero_aleatorio = random.randint(1,100)
numero_elegido = int(input('Escribe un numero del 1 al 100: '))

while numero_elegido != numero_aleatorio:
    if numero_elegido < numero_aleatorio:
        numero_elegido = int(input('Busca un numero más grande: '))
    else:
       numero_elegido = int(input('Busca un numero más pequeño: '))
print('GANASTE!')