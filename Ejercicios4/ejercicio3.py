# Dada una lista de cadenas nos pida una cadena por teclado e indique si está en la lista, cuántas veces, lea otra cadena y la sustituya por la primera y borrar

lista1 = ["hola", "adios", "pepe"]

palabra = input("Introduzca una palabra: ")

if(palabra in lista1):
    print("Está en la lista.")
    print(lista1.count(palabra), "veces")
else:
    print("No está en la lista.")

palabraSustituir = input("Introduzca otra palabra: ")
lista1[0] = palabraSustituir
print(lista1)

