def sumarDosNumeros(num1, num2):
    return num1 + num2

def restarDosNumeros(num1, num2):
    return num1 - num2

def multiplicarDosNumeros(num1, num2):
    return num1 * num2

def dividirDosNumeros(num1, num2):
    if num2 == 0:
        return "No se puede dividir por 0"
    return num1 / num2

print("CALCULADORA PROGRAMADA POR PYTHON")

def menu():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    
    opcion = int(input("Elije una opcion: "))
    
    if opcion == 1:
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        
        print ("El resultado de la suma es: ", sumarDosNumeros(num1, num2))
    
    
    if opcion == 2:
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        
        print ("El resultado de la resta es: ", restarDosNumeros(num1, num2))
        
    if opcion == 3:
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        
        print ("El resultado de la multiplicacion es: ", multiplicarDosNumeros(num1, num2))
    
    if opcion == 4:
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        
        print("El resultado de la division es:  ", dividirDosNumeros(num1, num2))
        
        
        
menu()

print("Muchisimas gracias por usar esta calculadora :))")
