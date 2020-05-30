# Crear una función que dependiendo de los parámetros que reciba haga una de las dos funciones anteriores.

from funciones1 import calc1, calc2


def seleccion(*argumentos):
    if len(argumentos) == 1:
        return calc2(argumentos[0])
    elif len(argumentos) == 3:
        return calc1(argumentos[0], argumentos[1], argumentos[2])
    else:
        raise TypeError("Solo pueden ser 1 o 3 parámetros")


print(seleccion(10, 10, 2))
