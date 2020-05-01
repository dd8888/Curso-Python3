f=open("C:\\Users\\Shaco\\Documents\\CursoPython3\\Curso-Python3\\Ejercicios7\\prueba.txt", "r")
# read() lee el archivo
# readline() lee una linea
# readlines() lee todas las lineas y las devuelve como lista
# write() escribe en el archivo
print(f.read())

# seek(0) mueve el puntero al principio del fichero
# close() cierra el archivo
f.close()