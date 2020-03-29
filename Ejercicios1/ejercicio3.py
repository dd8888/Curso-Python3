# Calcular perimetro y area de un circulo dado su radio
import math
radio = input("Introduzca el radio: ")

perimetro = math.pi * 2 * float(radio)

print("El perimetro es:", perimetro)

area = math.pi * float(radio)**2

print("El area es:", area)