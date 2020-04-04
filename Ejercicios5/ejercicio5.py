# Determinar si una palabra es un palíndromo

palabra = input("Introduzca una palabra: ")

for i in range(int(len(palabra)/2)):
    if palabra[i] == palabra[(len(palabra) - i) - 1]:
        continue
    else:
        print("NO es un palíndromo")
        break
else:
    print("Es un palindromo")



