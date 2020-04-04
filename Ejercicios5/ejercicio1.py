# Ejercicio que pida una cadena y un caracter e inserte el caracter entre cada letra de la cadena

cadena = input("Introduzca una cadena: ")
caracterIn = input("Introduzca un caracter: ")

for i in range(len(cadena)):
    print(cadena[i] + "" + caracterIn, end = "")

# También se puede hacer así
print()
print(caracterIn.join(cadena))