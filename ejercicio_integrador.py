productos = [["Maiz grano",285.55],
             ["Pepino",334.72], 
             ["Tomate verde",129.0]
             ]

venta_productos = [
[2, 122],
[1, 89],
[1, 22],
[3, 48],
[1, 75],
[3, 322],
[2, 95],
[1, 148],
[1, 83],
[3, 100]
]

ventas_dia = 0

for i in venta_productos:
     ventas_dia += i[1]

cajas_venta = int(input("Numero de cajas a vender: "))
id_producto = input("ID del producto: ")

ventas_para_descuento = 1500
venta_total = ventas_dia + cajas_venta
descuento = venta_total > ventas_para_descuento 

if id_producto == "1":
    print("El producto es:", productos[0][0])
    print("El precio por caja es:", productos[0][1])
    print("Aplica descuento del 20%:", descuento)
    if descuento:
        print("El costo total a pagar:", round((productos[0][1] * cajas_venta)*(0.8), 2))
    else:
        print("El costo total a pagar:", round((productos[0][1] * cajas_venta), 2))
elif id_producto == "2":
    print("El producto es:", productos[1][0])
    print("El precio por caja es:", productos[1][1])
    print("Aplica descuento del 20%:", descuento)
    if descuento:
        print("El costo total a pagar:", round((productos[1][1] * cajas_venta)*(0.8),2))
    else:
        print("El costo total a pagar:", round((productos[1][1] * cajas_venta),2))
elif id_producto == "3":
    print("El producto es:", productos[2][0])
    print("El precio por caja es:", productos[2][1])
    print("Aplica descuento del 20%:", descuento)
    if descuento:
        print("El costo total a pagar:", round((productos[2][1] * cajas_venta)*(0.8), 2))
    else:
        print("El costo total a pagar:", round((productos[2][1] * cajas_venta), 2))
else:
    print("ID NO VALIDO")