import random

print("GENERADOR DE CONTRASEÑAS CON PYTHON !!")

longitud = int(input("INGRESE LA LONGITUD DE LA CONTRASEÑA QUE DESEA GENERAR: "))

contraseña = random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!?", k=longitud)

print("La contraseña generada es: " + "".join(contraseña))

