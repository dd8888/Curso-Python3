# Programa que agregue a un diccionario personas y sus gustos

gustos={}
nombre = input("Nombre:")
while nombre!="*":
    gusto=input("Gusto:")
    lista_gustos=gustos.setdefault(nombre,[gusto])
    if lista_gustos!=[gusto]:
        gustos[nombre].append(gusto)
    nombre = input("Nombre:")
print(gustos)   