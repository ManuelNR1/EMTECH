paises = ('Mexico', 'Canada', 'China', 'Japon')
importaciones = (430, 560, 310, 695)
exportaciones = (1932, 3540, 4800, 530)

agrupacion = list(zip(paises, importaciones, exportaciones))

agrupacion1 = tuple(zip(paises, importaciones, exportaciones))

agrupacion2 = set(zip(paises, importaciones, exportaciones))

print(agrupacion)
print(agrupacion1)
print(agrupacion2)

print(dict(zip(paises, exportaciones)))

print(list(zip(*paises)))

for pais, exportacion in zip(paises, exportaciones):
    print(pais, exportacion)