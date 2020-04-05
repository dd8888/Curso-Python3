# Programa que lea una cadena y devuelva un diccionario con las apariciones de cada palabra en la cadena

cadena = input("Introduzca una frase: ")

dict1 = {}
lista = cadena.split(" ")
contador = 0
for palabra in lista:
    if palabra in dict1:
        dict1[palabra] += 1
    else:
        dict1[palabra] = 1
    
for i, h in dict1.items():
    print(i, "->", h)