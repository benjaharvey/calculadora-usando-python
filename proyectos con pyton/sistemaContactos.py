# Sistema de contactos utilizando archivos de texto en Python :D
# Utilize un dataclass ya que, segun lo que encontre en internet, es lo mas parecido a un typedef struct de C, que es lenguaje al cual estoy mas acostumbrado a programar
from dataclasses import dataclass

  
@dataclass
class contacto:
    nombreApellido: str
    email: str
    numTelefono: str

def agregarContacto():
  with open("archivoContactos.txt", "a") as archivoContacto:
    nuevoNombre = input("Ingrese el nombre y apellido del contacto que desea ingresar: ")
    nuevoEmail = input("Ingrese el email del contacto que desea agregar: ")
    nuevoTelefono = input("Ingrese el telefono del nuevo contacto: ")
    
    nuevoContacto = contacto(nuevoNombre, nuevoEmail, nuevoTelefono)
    
    archivoContacto.write(f"{nuevoContacto.nombreApellido}, {nuevoContacto.email}, {nuevoContacto.numTelefono}\n")
    
    print("Contacto almacenado de forma exitosa")
 

 
def buscarContacto():
  with open("archivoContactos.txt", "r") as archivoContacto:
    busqueda = input("Ingrese el numero de telefono del contacto que desee buscar: ")
    encontrado = False
    for linea in archivoContacto:
      
      if busqueda in linea:
        print(f"Contacto encontrado!, {linea.strip()}")
        encontrado = True
        break
    
    if encontrado == False:
      print("No existe ese contacto!")



def visualizarTodos():
  with open("archivosContactos.txt", "r") as archivoContacto:
    
    try:
     print("Los contactos que estan en el sistema son los siguientes: ")
     for lineas in archivoContacto:
      print(lineas)
    
    except FileNotFoundError:
      print("El archivo no existe!, crealo usando la opcion 1")

def menu():
  opcion = int(input("1- ingresar contacto; 2- buscar contacto; 3- visualizar todos los contactos; 4- eliminar contacto especifico; 5- eliminar todos: "))
  
  if opcion == 1:
    agregarContacto()
  
  if opcion == 2:
    buscarContacto()
  
  if opcion == 3:
    visualizarTodos()    


menu()