## Ejemplo de módulo

def cuadrado(n):
    return (n**2)
def cubo(n):
    return (n**3)

## Esto permite ejecutar el módulo como un script
if __name__ == "__main__":
    print(cuadrado(3))
    print(cubo(3))