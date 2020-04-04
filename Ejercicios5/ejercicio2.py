# Programa que sustituya los dígitos de una cadena por un caracter

cadena = input("introduzca una cadena: ")
car = input("introduzca un caracter: ")

for i in range(10):
    cadena = cadena.replace(str(i), car)

print(cadena)