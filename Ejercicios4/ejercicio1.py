# Leer por teclado numeros y guardarlos en una lista. Finaliza cuando se introduce uno negativo. Muestra el máximo y los pares.

esPositivo = True
lista = []
while(esPositivo):
    numero = int(input("Introduzca un numero: "))
    if numero > 0:
        lista.append(numero)
    else:
        esPositivo = False
        print("El numero mas grande es:",max(lista))
        for i in lista:
            if i % 2 == 0:
                print(i)
