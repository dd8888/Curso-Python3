# Escribir un programa que dada dos cadenas de caracteres indique si la segunda es una subcadena de la primera y devuelva la que sea anterior en orden alfabético

cad1 = input("Cadena 1: ")
cad2 = input("Cadena 2: ")

if(cad1.find(cad2) > -1):
    print("Es una subcadena.")
else:
    print("No es una subcadena")

if cad1 < cad2:
    print(cad1)
else: 
    print(cad2)
