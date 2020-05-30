# Una lista que añada contactos a una agenda (diccionario) con el nombre y el teléfono
from funciones4 import busqueda

def guardar_agenda(l_agenda, **kwargs):
    l_agenda.append(kwargs)
    return l_agenda

def main():
    agenda = []
    cantidad = int(input("Cuántos contactos? "))
    for i in range(cantidad):
        contacto = {}
        contacto["nombre"] = input("Indica el nombre: ")
        contacto["numero"] = input("Indica el telefono: ")
        campo = input("Introduzca otro campo: ")
        while campo != "*":
            contacto[campo] = input("Introduzca valor: ")
            campo = input("introduzca otro campo: ")
        agenda = guardar_agenda(agenda, **contacto)

    parametro = input("Introduzca el param de busqueda: ")    
    busqueda(parametro, agenda)


main()