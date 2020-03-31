# Aplicacion que pida un numero y devuelva su factorial

numero = int(input("Introduzca un numero: "))

for i in range(1, numero):
    numero = numero * i
print (numero)