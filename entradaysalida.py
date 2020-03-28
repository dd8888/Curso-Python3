# La función "input()" se usa para pedir por teclado.
num1 = input("Dame el numero 1: ")
num2 = input("Dame el numero 2: ")

# Para concatenar texto tengo que convertir las variables a texto usando la función "str()". 
# Para convertir texto a int se usa "int()".
print("El resultado es " + str(int(num1) + int(num2)))


# También se puede concatenar usando la coma.
print("El resultado es" , int(num1) + int(num2))
suma = int(num1) + int(num2)

# Se puede usar la función format() para el formato de las variables de salida
print(format(suma, "x"), "es el numero ", suma, "en hexadecimal")