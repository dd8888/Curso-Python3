# Programa de login
usuario = "David"
contraseña = "1234"

inputusuario = input("Introduzca su usuario: ")
inputcontraseña = input("Introduzca su contraseña: ")

if inputusuario == usuario and inputcontraseña == contraseña:
    print("Login correcto")
else:
    print("Login incorrecto")