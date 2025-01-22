# creando una lista con list()
lista = list(["hola", "benja", 34])
print(lista)

#devuelve cantidad de elementos en la lista
resultado = len(lista)
print(resultado)

#agrega un elemento al final de la lista
lista.append("chadbenja")

print(lista)

#agregando un elemento a la lista usando un indice especifico
lista.insert(1, "rayven sos horrible")

print(lista)

#agregando varios elementos a la lista
lista.extend(["Hola chads", "me llamo kanye", 10])

print(lista)

#eliminamos elemento de la lista usando un indice
lista.pop(3) #-1 para ultimo, -2 para anteultimo, etc

print(lista)

#eliminamos elemento de la lista usando el valor
lista.remove("hola")

print(lista)

#elimina todos los elementos de la lista
# lista.clear()

# print(lista)

#ordenar lista de menor a mayor (si usamos reverse = true lo ordena de mayor a menor)
lista2 = list([34,12,99,115,3])
print(lista2)

list.sort(lista2)

print(lista2)

#verificar si el elemento existe en la lista
elementoEncontrado = lista.index("me llamo kanye")
print(elementoEncontrado)

