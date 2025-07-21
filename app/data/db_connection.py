## Funcion para crear y abrir la conexion a la base de datos Mysql.
# Sera llamada desde otros archivos para generar las consultas correspondientes.

import mysql.connector
from app.data.credentials import config
import datetime

def crear_conexion():
    try: 
        conexion = mysql.connector.connect(**config)
        if conexion.is_connected():
            #print("Conexion Exitosa.")
            return conexion # base de datos conectada exitosamente

    except mysql.connector.Error as err:
        fecha_hora=datetime.datetime.now().strftime("[%d/%m/%Y - %H:%M:%S]")
        file = open("error-db.txt", "a") 
        file.writelines(f"{fecha_hora} | Error: {err} \n") # se escribe el error en el archivo error-db.txt
        #print("Conexion fallida. Ver error-db.txt")
        return None # no retorna nada