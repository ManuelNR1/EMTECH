from operator import itemgetter

#Lista que contendrá los detalles ingresados por el pasajero
pasajeros = {}



opcion = input("Bienvenido a FlyUs-México\n(1) Añadir cliente\n(2) Listar todos los clientes\n(3) Listar clientes preferentes\n(4) Salir\nSeleccione una opción: ")
if opcion == "1":
    while 1==1:
        id = input("\nIngresa el ID del INE: ")

        nombre = input("Ingresa el nombre: ")
        
        edad = int(input("Ingresa la edad: "))

        destino = input("IATA del Destino: ")
        while destino != 'GDL' and destino != 'BJX' and destino != 'JAL':
            destino = input('IATA del destino no válida, ingresar nueva IATA: ')

        cliente_preferente = input("Cliente preferente (Si/No): ")
        if cliente_preferente == "Si" or cliente_preferente == "si" or cliente_preferente == "SI":
            cliente_preferente = True
        else:
            cliente_preferente = False
            
        continuar = input("¿Desea añadir otro cliente? (Si/No): ")
        if continuar != "Si" or continuar != "si" or continuar != "SI":
            break

    print(cliente_preferente)