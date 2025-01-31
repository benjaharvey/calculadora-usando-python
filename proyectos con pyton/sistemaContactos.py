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
  try:
    print("Los contactos en el sistema son los siguientes\n")
    
    with open("archivoContactos.txt", "r") as archivoContactos:
      for linea in archivoContactos:
        print(linea)
  
  
  except FileNotFoundError:
    print("No existe el archivo!")


def  eliminarUnContacto():
  with open("archivoContactos.txt", "r") as archivoContacto:
    lineasArchivo = archivoContacto.readlines()
    
    eliminar = input("ingrese el numero telefonico que desea eliminar: ")
    encontrado = False
    
    with open("archivoContactos.txt", "w") as archivoContactos:
      for linea in lineasArchivo:
        if eliminar not in linea:
          archivoContactos.write(linea)
        else:
          encontrado = True
      
      if(encontrado == True):
        print("Contacto eliminado de forma exitosa")
      else:
        print("No se encontro el contacto que desea eliminar")


def eliminarTodos():
  with open("archivosContactos.txt", "w") as archivoContacto:
    pass
  
  print("Todos los contactos fueron eliminados!")

def menu():
  while True:
    print("-- /SISTEMA DE CONTACTOS HECHO EN PYTHON\ --")
    
    print("1; Agregar Contactos")
    print("2; Visualizar Contactos")
    print("3; Buscar Contacto")
    print("4; Eliminar un contacto especifico")
    print("5; Eliminar todos los contactos")
    print("0; Salir del programa")
    
    opcion = input("Ingrese la opcion deseada: ")
    
    if opcion == 1:
      agregarContacto()
    
    if opcion == 2:
      visualizarTodos()
    
    if opcion == 3:
      buscarContacto()
    
    if opcion == 4:
      eliminarUnContacto()
    
    if opcion == 5:
      eliminarTodos()
    
    if opcion == 6:
      print("Gracias por usar mi programa :D -- Escrito por Benjamin J.A. Harvey usando de ayuda Copilot AI para la funcion de eliminar un contacto -- 30/1/25")
      break


menu()