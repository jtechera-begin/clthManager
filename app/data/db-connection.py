## Funcion para crear y abrir la conexion a la base de datos Mysql.
# Sera llamada desde otros archivos para generar las consultas correspondientes.

import mysql.connector
from credentials import config 

def crear_conexion():
    try: 
        conexion = mysql.connector.connect(**config)
        if conexion.is_connected():
            print("Conexion Exitosa.")
            return conexion # base de datos conectada exitosamente

    except mysql.connector.Error as err:
        file = open("error-db.txt", "w") 
        file.write(f"Error: {err}") # se escribe el error en el archivo error-db.txt
        print("Conexion fallida. Ver error-db.txt")
        return None # no retorna nada
    
crear_conexion()