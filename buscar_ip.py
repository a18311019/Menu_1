import argparse
import socket

# Definir el argumento para la URL
def parsear_argumentos():
    parser = argparse.ArgumentParser(description="Obtener la IP de un dominio.")
    parser.add_argument("-t", "--target", help="Ingresa la dirección: ", required=True)
    return parser.parse_args()

# Función para obtener la IP de una URL
def obtener_ip(dominio):
    try:
        ip = socket.gethostbyname(dominio)
        print(f"La dirección IP de {dominio} es: {ip}")
    except socket.gaierror:
        print(f"No se pudo obtener la IP para {dominio}. Verifique la dirección o la conexión.")

# Función principal
def main():
    argumentos = parsear_argumentos()
    obtener_ip(argumentos.target)

# Ejecutar la función principal
if __name__ == "__main__":
    main()