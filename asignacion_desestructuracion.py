exportaciones = (850,920)

mexico, canada = exportaciones

print(mexico)
print(canada)

#Las tuplas se pueden escribir sin parentesis
china, japon = 1810, 1516

colombia, chile, brasil = [520, 630, 450]

print(brasil)

paises = [('Mexico', 850), ('Canadá', 920), ('China', 1940)]

for pais in paises:
    nombre = pais[0]
    total = pais[1]
    print(f'{nombre} realizó {total} exportaciones en 2019')

for nombre, total in paises:
        print(f'{nombre} realizó {total} exportaciones en 2019')