# Sistema de contactos utilizando archivos de texto en Python :D
# Utilize un dataclass ya que, segun lo que encontre en internet, es lo mas parecido a un typedef struct de C, que es lenguaje al cual estoy mas acostumbrado a programar
from dataclasses import dataclass

  
@dataclass
class contacto:
    nombreApellido: str
    email: str
    numTelefono: str


def agregarContacto():
  with open("archivoContactos.txt", "a") as archivoContactos:
    nombreApellido = input("Ingrese el nombre y apellido del contacto: ")
    email = input("Ingrese el email: ")
    numTelefono = input("Ingrese el numero de telefono: ")
    
    nuevoContacto = contacto(nombreApellido, email, numTelefono)
    
    archivoContactos.write(f"{nuevoContacto.nombreApellido}, {nuevoContacto.email}, {nuevoContacto.numTelefono}\n")
    
    print("Contacto añadido exitosamente!\n")
    
    
    
def mostrarContactos():
  with open("archivoContactos.txt", "r") as archivoContactos:
    for linea in archivoContactos:
      print(linea)

