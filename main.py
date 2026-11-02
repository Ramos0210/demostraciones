
import subprocess
import sys

while True:
    print("\n=== DEMOSTRACIONES ===")
    print("1. Mutabilidad")
    print("2. Programación asíncrona")
    print("3. seguridad web y almacenamiento persistente")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    archivos = {
        "1": "mutabilidad.py",
        "2": "asincronia.py",
        "3": "seguridad_web.py"
    }

    if opcion in archivos:
        subprocess.run([sys.executable, archivos[opcion]])
    elif opcion == "4":
        print("¡Fin de las demostraciones!")
        break
    else:
        print("Opción no válida")
