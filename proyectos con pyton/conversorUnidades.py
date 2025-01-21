def metrosKilometros(metros):
    return metros / 1000

def librasKilos(libras):
    return libras * 0.453592

def fahrenheitCelsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

opcion = int(input("INGRESE LA OPCION QUE DESEA\n 1. METROS A KILOMETROS \n 2. LIBRAS A KILOS \n 3. FAHRENHEIT A CELSIUS \n"))

if opcion == 1:
    metros = int(input("INGRESE LOS METROS QUE DESEA CONVERTIR: "))
    print("LOS METROS INGRESADOS SON EQUIVALENTES A " + str(metrosKilometros(metros)) + "KILOMETROS")
    
if opcion == 2:
    libras = int(input("INGRESE LAS LIBRAS QUE DESEA CONVERTIR: "))
    print("LAS LIBRAS INGRESADAS SON EQUIVALENTES A " + str(librasKilos(libras)) + "KILOS")

if opcion == 3:
    fahrenheit = int(input("INGRESE LOS GRADOS FAHRENHEIT QUE DESEA CONVERTIR: "))
    print("LOS GRADOS FAHRENHEIT INGRESADOS SON EQUIVALENTES A " + str(fahrenheitCelsius(fahrenheit)) + "CELSIUS")
    
 