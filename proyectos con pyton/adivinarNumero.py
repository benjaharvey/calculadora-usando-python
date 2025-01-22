# Haz un juego donde el programa elija un número aleatorio, y el usuario deba adivinarlo en un rango definido.

import random

numero = random.randint(1,20)

print("ADIVINA EL NUMERO QUE ESTOY PENSANDO ENTRE 1 Y 20, TENES 5 INTENTOS")
              
def adivinarNumero(numero):
    intentos = 5
    
    while intentos > 0:
        adivina = int(input("INGRESE EL NUMERO QUE CREE QUE ESTOY PENSANDO: "))
        
        if adivina == numero:
            print("EL NUMERO ERA " + str(numero) + " FELICITACIONES, ADIVINASTE CORRECTAMENTE")
            
        else:
            intentos -= 1
            print("TE QUEDAN " + str(intentos) + " INTENTOS, PROBA DEVUELTA")
            if(intentos == 0):
                print("EL NUMERO ERA " + str(numero) + " PERDISTE, NO ADIVINASTE EL NUMERO")
            
adivinarNumero(numero)

