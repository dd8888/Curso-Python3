# Dada una lista de números indique si la lista está ordenada o no

lista = [1, 2, 3, 4, 5, 6, 7, 1]
listaOrdenada = lista[:]
lista.sort()
if(lista == listaOrdenada):
    print("Está ordenada")
else:
    print("Está desordenada")
