productos = 21

caja_rapida = productos <= 10
caja_autocobro = productos < 26

print(caja_rapida)
print(caja_autocobro)

veinte_productos = productos == 20
print(veinte_productos)

numero_ganador = 23
numero_cliente = int(input("Adivina el numero ganador: "))

print(numero_ganador == numero_cliente)