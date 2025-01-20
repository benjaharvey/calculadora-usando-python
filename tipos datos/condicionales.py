print("CALCULADORA DE POBREZA!!!!")
ingresoMensual = int(input("INGRESE SUS GANANCIAS MENSUALES EN USD: "))

if ingresoMensual > 500:
    print("NO SOS POBREEE !!!")
    sosPobre = False
else:
    print("SOS POBRE :(")
    sosPobre = True



if sosPobre == True:
    print("SI SOS POBRE TE DAMOS UNA AYUDA DE 100 USD")
    ingresoMensual += 100    

print("TUS GANANCIAS MENSUALES SON: ", ingresoMensual)

print("GRACIAS POR USAR NUESTRA CALCULADORA DE POBREZA")