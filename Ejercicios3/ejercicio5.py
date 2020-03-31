# Programa que pide un numero por teclado y dice si es primo o no

num = int(input("Introduzca un número: "))
esPrimo = True
for cont in range(2, num):
    if(num % cont == 0):
        esPrimo = False
        break
if esPrimo:
    print("Es primo")
else:
    print("No es primo")

