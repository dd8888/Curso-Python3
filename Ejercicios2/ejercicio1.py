# Programa que pida 2 números e indice si la suma es positiva negativa o 0

numero1 = float(input("Introduzca el primer numero: "))
numero2 = float(input("Introduzca el segundo numero: "))

if(numero1 + numero2 > 0):
    print("Es positivo")
elif(numero1 + numero2 < 0):
    print("Es negativo")
else:
    print("Es 0")