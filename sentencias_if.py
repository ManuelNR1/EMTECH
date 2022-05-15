
productos_descuento = ["Computadora", "TV", "Teclado", "Mouse",
"Laptop", "Monitor"]

sin_stock = ["Camara", "Celular", "Reloj", "Memoria"]

producto = input("Ingresa producto: ")

if producto in productos_descuento:
  print("Este producto tiene descuento!")
  print("Aprovecha la oferta")
elif producto in sin_stock:
    print("Producto Agotado")
else:
    print("No vendemos estas cosas!")

print("Fin de la sentencia if")
