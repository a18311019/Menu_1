import subprocess
import time

def mostrar_menu():
    opciones = [
        "1. Encontrar IP Socket",
        "2. Encontrar IP Comando CLI",
        "3. Banner Grabbing",
        "4. Escaneo de puertos",
        "0. Salir"
    ]
    print("\n=== Menú ===")
    for opcion in opciones:
        print(opcion)

def ejecutar_comando(comando):
    try:
        resultado = subprocess.run(comando, shell=True, check=True)
        return resultado
    except subprocess.CalledProcessError as error:
        print(f"Error al ejecutar el comando: {comando}")
        print(f"Detalles: {error}")

def obtener_dominio():
    while True:
        dominio = input("Ingresa la dirección (o escribe 'volver' para regresar al menú): ").strip()
        if dominio.lower() == 'volver':
            return None
        if dominio:
            return dominio
        print("Por favor, ingresa una dirección válida.")

def obtener_puerto():
    while True:
        puerto = input("Ingresa el puerto (o escribe 'volver' para regresar al menú): ").strip()
        if puerto.lower() == 'volver':
            return None
        if puerto.isdigit():
            return puerto
        print("Por favor, ingresa un número válido para el puerto.")

def ejecutar_opcion(opcion):
    if opcion == '1':
        print("Opción 1: Encontrar IP Socket")
        dominio = obtener_dominio()
        if dominio:
            ejecutar_comando(f"python buscar_ip.py -t {dominio}")

    elif opcion == '2':
        print("Opción 2: Encontrar IP Comando CLI")
        dominio = obtener_dominio()
        if dominio:
            ejecutar_comando(f"python encontrar_cli.py -t {dominio}")

    elif opcion == '3':
        print("Opción 3: Banner Grabbing")
        dominio = obtener_dominio()
        if dominio:
            puerto = obtener_puerto()
            if puerto:
                ejecutar_comando(f"python banner_grabbing.py -t {dominio} -p {puerto}")

    elif opcion == '4':
        print("Opción 4: Escaneo de puertos")
        dominio = obtener_dominio()
        if dominio:
            ejecutar_comando(f"python escanear_puertos.py -t {dominio}")

    elif opcion == '0':
        print("Saliendo del menú...")

    else:
        print("Opción no válida. Por favor, elige de nuevo.")

def menu():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()
        if opcion == '0':
            ejecutar_opcion(opcion)
            break
        ejecutar_opcion(opcion)

menu()