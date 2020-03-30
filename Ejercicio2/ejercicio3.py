# Programa que pida un numero entero entre 1 y 12 e imprima el numero de dias que tiene el mes correspondiente

numero = (int(input("Introduzca el numero: ")))

if numero == 1:
    print("31")
elif numero == 2:
    print("28")
elif numero == 3:
    print("31")
elif numero == 4:
    print("30")
elif numero == 5:
    print("31")
elif numero == 6:
    print("30")
elif numero == 7:
    print("31")
elif numero == 8:
    print("31")
elif numero == 9:
    print("30")
elif numero == 10:
    print("31")
elif numero == 11:
    print("30")
elif numero == 12:
    print("31")


###############################################

if numero == 1 or numero == 3 or numero == 5 or numero == 7 or numero == 8 or numero == 10 or numero == 12:
    print("31 dias")
elif numero == 4 or numero == 6 or numero == 9 or numero == 11:
    print("30 dias")
else:
    print("28 dias o 29 dias")