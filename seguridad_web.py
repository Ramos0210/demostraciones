
import json

# Guardar información
datos = {"nombre": "Andrés"}

with open("datos.json", "w") as archivo:
    json.dump(datos, archivo)

# Recuperar información
with open("datos.json", "r") as archivo:
    informacion = json.load(archivo)

print("Información guardada:")
print(informacion["nombre"])
