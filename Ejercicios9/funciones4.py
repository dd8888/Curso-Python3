#Busqueda de contactos del método anterior
def busqueda(parametro, agenda):
    for contacto in agenda:
        if parametro == contacto["nombre"] or parametro == contacto["numero"]:
            print(contacto)