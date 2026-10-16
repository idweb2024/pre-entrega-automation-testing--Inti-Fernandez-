import csv
import pathlib
import json 

def leer_csv_login(ruta_archivo):
    """Lee el CSV de login y devuelve una lista de tuplas para parametrize."""
    datos = []
    ruta = pathlib.Path(ruta_archivo)

    with open(ruta, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            debe_funcionar = fila['debe_funcionar'].lower() == 'true'
            datos.append((fila['usuario'], fila['clave'], debe_funcionar, fila['descripcion']))

    return datos


if __name__ == "__main__":
    print(leer_csv_login("datos/login.csv"))




def leer_json_productos(ruta_archivo): 
    """ 
    Lee un archivo JSON con información de productos 
    """ 
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo: 
        productos = json.load(archivo) 
        # Extraigo los datos completos de los productos
    return productos

if __name__ == "__main__": 
    print(leer_json_productos('datos/productos.json')) 
