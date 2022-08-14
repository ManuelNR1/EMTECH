clientes = {45471: ["Luis Pérez", 45, "BJX", True], 8944411: ["Fernanda Garcia", 25, "JAL",True], 15223: ["Alejandra Ortíz", 33, "GDL",True]}
lista_pasajeros = []
lista_preferentes = []

def agregarClientes():
    while 1==1:
            i1, i2 = 0, 0
            while i1 == i2:
                try:
                    id = int(input("Ingresa el ID del INE: "))
                    i1 += 1
                except ValueError:
                    print("\nERROR, ingresa ID válido.")

            nombre = input("Ingresa el nombre: ")
            
            i3, i4 = 0, 0
            while i3 == i4:
                try:
                    edad = int(input("Ingresa la edad: "))
                    i3 += 1
                except ValueError:
                    print("\nERROR, ingresa numero entero.")
                  
            destino = input("IATA del Destino: ")
            while destino != 'GDL' and destino != 'BJX' and destino != 'JAL':
                destino = input('IATA del destino no válida, ingresar nueva IATA: ')

            cliente_preferente = input("Cliente preferente (Si/No): ")
            if cliente_preferente == "Si" or cliente_preferente == "si" or cliente_preferente == "SI":
                cliente_preferente = True
            else:
                cliente_preferente = False
            
            clientes[id] = [nombre, edad, destino, cliente_preferente]
            
            continuar = input("¿Desea añadir otro cliente? (Si/No): ")
            i5, i6 = 0, 0
            while True:
                if continuar == "Si" or continuar == "si" or continuar == "SI":
                    break
                elif continuar == "No" or continuar == "no" or continuar == "NO":
                    i5 += 1
                    break
                else:
                    continuar = input("Ingresa una opcion valida: ")
            if i5 != i6:
                print("\n")
                break

def eliminarClientes():
    i7, i8 = 0, 0
    while i7 == i8:
        try:
            id_eliminado = int(input("\nIngresa ID del INE: "))
            i7 += 1
        except ValueError:
            print("\nERROR, ingresa ID válido.")
    print("\n'"+clientes[id_eliminado][0]+"' se ha borrado de la lista\n")
    clientes.pop(id_eliminado)

def mostrarClientes():
    lista_pasajeros.clear() 
    for id, datos in clientes.items():
        lista_pasajeros.append([id, datos[0]])
    print("\nLista de todos los clientes:\n", lista_pasajeros,"\n")

def mostrarPreferentes():
    lista_preferentes.clear()
    for id, datos in clientes.items():
        if datos[3]:
            lista_preferentes.append([id, datos[0]])      
    print("\nLista de clientes preferentes:\n", lista_preferentes,"\n")

def edadPromedio():
    edades_clientes = 0
    for id, datos in clientes.items():
        edades_clientes += datos[1]
    try:
         edad_promedio = edades_clientes / len(clientes)
    except ZeroDivisionError:
         edad_promedio = 0
    print("\nLa edad promedio de los clientes es:", round(edad_promedio,1),"\n")

def edadPreferentes():
    edades_preferentes = 0
    contador_preferentes = 0
    for id, datos in clientes.items():
        if datos[3]:
            contador_preferentes += 1
            edades_preferentes += datos[1]
    try:
        edad_promedio_preferentes = edades_preferentes / contador_preferentes
    except ZeroDivisionError:
        edad_promedio_preferentes = 0
    print("\nLa edad promedio de los clientes preferentes es:", round(edad_promedio_preferentes,1),"\n")

while True:
    opcion = input("Bienvenido a FlyUs-México\n(1) Añadir cliente\n(2) Listar todos los clientes\n(3) Listar clientes preferentes\n(4) Eliminar un cliente mediante ID del INE\n(5) Edad promedio de todos los clientes\n(6) Edad Promedio de clientes preferentes\n(7) Salir\nSeleccione una opción: ")

    if opcion == "1":
       agregarClientes()
                        
    elif opcion == "2":
       mostrarClientes()

    elif opcion == "3":
       mostrarPreferentes()
    
    elif opcion == "4":
        eliminarClientes()

    elif opcion == "5":
        edadPromedio()

    elif opcion == "6":
        edadPreferentes()
    
    elif opcion == "7":
        print("\n¡Adios!\n")
        break

    else:
        print("\nIngresa una opción valida\n")