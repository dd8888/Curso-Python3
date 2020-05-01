import csv
f=open("C:\\Users\\Shaco\\Documents\\CursoPython3\\Curso-Python3\\Ejercicios7\\ejemplo1.csv", "r")
contenido = csv.reader(f)
lista = list(contenido)
print(lista)
f.seek(0)

for row in contenido:
    print(str(row))

f.close()