# Programa para adivinar numero
import random

numeroAleatorio = random.randrange(10)

acierto = False

while acierto == False:
    numero = int(input("Introduzca un numero: "))
    if numero == numeroAleatorio:
        print("Acertaste!")
        acierto = True
    elif numero > numeroAleatorio:
        print ("Tu numero es mayor")
    else:
        print ("Tu numero es menor")