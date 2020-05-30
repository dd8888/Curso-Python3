#Funcion recursiva que multiplique los elementos de una lista

def func(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista.pop() * func(lista)

print(func([3, 4, 5]))