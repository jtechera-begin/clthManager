## CONSULTA PARA LLENAR EL DATA GRID VIEW EN CLIENTES

from app.data.db_connection import crear_conexion
import datetime
import mysql.connector

def cargar_datos():
    conexion = crear_conexion()
    if conexion is None:
        return None
    else:
        try:
            cursor = conexion.cursor(dictionary=True)
            query = "SELECT ID, nombre, correo, telefono, direccion, debe FROM cliente WHERE activo = 1;"
            cursor.execute(query)
            resultados = cursor.fetchall()

            return resultados if resultados else []  # Retorna lista vacía si no hay datos

        except Exception as e:
            fecha_hora = datetime.datetime.now().strftime("[%d/%m/%Y - %H:%M:%S]")
            with open("app/data/error-db.txt", "a") as file:
                file.writelines(f"{fecha_hora} | Error: {e} \n")
            return None ## Devuelve none si solo si hay una excepcion 
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()

def ingresar_datos(nombre, correo, telefono, direccion, observaciones, notificaciones):
    conexion = crear_conexion()
    if conexion is None:
        return -1
    else:
        try:
            cursor = conexion.cursor()
            query = """
                INSERT INTO cliente 
                (nombre, correo, telefono, direccion, observaciones, notificaciones)
                VALUES (%s, %s, %s, %s, %s, %s);
            """
            valores = (nombre, correo, telefono, direccion, observaciones, notificaciones)
            cursor.execute(query, valores)
            conexion.commit()
            return 0

        except mysql.connector.ProgrammingError:
            return 1  # Código 1: error de sintaxis SQL o tabla inexistente
        except Exception as e:
            fecha_hora = datetime.datetime.now().strftime("[%d/%m/%Y - %H:%M:%S]")
            with open("app/data/error-db.txt" , 'a') as f:
                f.writelines(f"{fecha_hora} | Error: {e} \n")
            return 2  # Código 2: otro error inesperado
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()