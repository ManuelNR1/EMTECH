#El estado de sinaloa cuenta con una superficie de 57365 km2
#Se localiza al noroeste del pais
#Clima principalmente calido, subhumedo, seco y semiseco
#Temperatura media anual de 25.45 grados celsius
#Precipitacion anual promedio de 790.1 mm

#Poblacion de 1532128 mujeres y 1494815 hombres
#Porcentaje habitantes de 33.15% en Culiacan y 16.15 en Mazatlan

territorio_km = 57365
localizacion = "Noroeste"
climas = ["Calido", "Humedo", "Seco", "Semiseco"]
temp_media_anual_celsius = 22.45
precipitacion_anual_prom_mm = 790.1

poblacion_mujeres = 1532182
poblacion_hombres = 1494815

habitantes_Culiacan_porcentaje = 33.15
habitantes_Mazatlan_porcentaje = 16.57

#Poblacion total entre hombres y mujeres
poblacion_total = poblacion_mujeres + poblacion_hombres
print("Poblacion total:", poblacion_total, "habitantes")

#Porcentaje total de poblacion entre Cln y Maza
porcentaje_total_habitantes = habitantes_Culiacan_porcentaje + habitantes_Mazatlan_porcentaje
print("Porcentaje habitacional total entre Culican y Mazatlan: ", porcentaje_total_habitantes, "%")

#Temperatura media anual y tipos de climas
climas.append(temp_media_anual_celsius)
print(climas)