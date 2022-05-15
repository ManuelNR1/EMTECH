carrito_compras = []

agregar_producto = input("Deseas agregar un producto? (si/no): ")

while agregar_producto == "si":
    nuevo_producto = input("Ingresa el producto: ")
    carrito_compras.append(nuevo_producto)
    agregar_producto = input("¿Deseas agregar otro producto? (si/no): ")

print(carrito_compras)