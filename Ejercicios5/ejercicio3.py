# Programa que lea una cadena de caracteres y muestre; la primera letra de cada palabra, primera letra de cada palabra en mayuscula, palabras que empiezan con "a"

cadena = input("Introduzca una cadena: ")

lista = cadena.split(" ")
for i in lista:
    if i.startswith("a"):
        print(i, end = " ")
print()
for i in lista:
    print(i.capitalize(), end = " ")

print()
for i in lista:
    print(i[0], end=" ")



