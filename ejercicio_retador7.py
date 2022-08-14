datos_pasajeros = {}
lista_pasajeros = []
lista_preferentes = []

while True:
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
            
            datos_pasajeros[id] = [nombre, edad, destino, cliente_preferente]
            
            continuar = input("¿Desea añadir otro cliente? (Si/No): ")
            if continuar == "Si" or continuar == "si" or continuar == "SI":
                continue
            elif continuar == "No" or continuar == "no" or continuar == "NO":
                print("\n")
                break

    elif opcion == "2":
       lista_pasajeros.clear() 
       for id, datos in datos_pasajeros.items():
        lista_pasajeros.append([id, datos[0]])
    
       print("\nLista de todos los clientes:\n", lista_pasajeros,"\n")  

    elif opcion == "3":
       lista_preferentes.clear()
       for id, datos in datos_pasajeros.items():
        if datos[3]:
            lista_preferentes.append([id, datos[0]])
            
       print("\nLista de clientes preferentes:\n", lista_preferentes,"\n")
    
    elif opcion == "4":
        print("Adios!")
        break