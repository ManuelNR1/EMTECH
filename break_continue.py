autos = ["correcto", "correcto", "correcto", "defectuoso",
"correcto", "correcto"]

for estado in autos:
    if estado == "defectuoso":
        print("Auto defectuoso, REVISION")
        continue
        #break
    print("Este auto está: " + estado)
    print("Enviando a distribucion")


for estado in autos:
    if estado == "defectuoso":
        print("Auto defectuoso, PARAR PRODUCCION")
        break
    print("Este auto está: " + estado)
    print("Enviando a distribucion")
