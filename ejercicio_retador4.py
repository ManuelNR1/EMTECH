productos = [["Maiz grano",285.55],
             ["Pepino",334.72], 
             ["Tomate verde",129.0]
             ]

#ventas_productos = [[122],
 #                   [89],
  #                  [22],
   #                 [48],
    #                [75],
     #               [322],
      #              [95],
       #             [148],
        #            [83],
         #           [100],
          #          ]

#total_productos_vendidos = sum(ventas_productos)
#print(total_productos_vendidos)

cajas_venta = int(input("Numero de cajas a vender: "))
id_producto = input("ID del producto: ")

ventas_para_descuento = 1500
ventas_dia = 1104
venta_total = ventas_dia + cajas_venta
descuento = venta_total > ventas_para_descuento 

if id_producto == "1":
    print("El producto es:", productos[0][0])
    print("El precio por caja es:", productos[0][1])
    print("Aplica descuento del 20%:", descuento)
    if descuento:
        print("El costo total a pagar:", (productos[0][1] * cajas_venta)*(0.8))
    else:
        print("El costo total a pagar:", (productos[0][1] * cajas_venta))
elif id_producto == "2":
    print("El producto es:", productos[1][0])
    print("El precio por caja es:", productos[1][1])
    print("Aplica descuento del 20%:", descuento)
    if descuento:
        print("El costo total a pagar:", (productos[1][1] * cajas_venta)*(0.8))
    else:
        print("El costo total a pagar:", (productos[1][1] * cajas_venta))
elif id_producto == "3":
    print("El producto es:", productos[2][0])
    print("El precio por caja es:", productos[2][1])
    print("Aplica descuento del 20%:", descuento)
    if descuento:
        print("El costo total a pagar:", (productos[2][1] * cajas_venta)*(0.8))
    else:
        print("El costo total a pagar:", (productos[2][1] * cajas_venta))
else:
    print("ID NO VALIDO")