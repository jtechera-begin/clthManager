## CONSULTA PARA LLENAR EL DATA GRID VIEW EN CLIENTES

from app.data.db_connection import crear_conexion
import datetime

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
            with open("error-db.txt", "a") as file:
                file.writelines(f"{fecha_hora} | Error: {e} \n")
            return None ## Devuelve none si solo si hay una excepcion 
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()