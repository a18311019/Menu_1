import sys
import argparse
import subprocess

# Definir y obtener los argumentos
def parsear_argumentos():
    parser = argparse.ArgumentParser(description="Obtiene la IP de un dominio o IP usando nslookup.")
    parser.add_argument('-t', '--target', help='Introduce la dirección IP o dominio de la víctima', required=True)
    return parser.parse_args()

# Función para obtener la IP con nslookup
def obtener_ip(target):
    try:
        # Usar subprocess para capturar la salida de nslookup
        resultado = subprocess.run(['nslookup', target], capture_output=True, text=True, check=True)
        print(resultado.stdout)
    except subprocess.CalledProcessError as e:
        print('[-] No se pudo obtener la IP con nslookup.')
        print(f"Detalles: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"[-] Ocurrió un error inesperado: {e}")
        sys.exit(1)

# Función principal
def main():
    args = parsear_argumentos()
    obtener_ip(args.target)

# Punto de entrada del programa
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Programa interrumpido por el usuario.")
        sys.exit(0)