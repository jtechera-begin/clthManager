from app.data.db_connection import crear_conexion
import datetime

def iniciar_sesion(user, passwd):
    conexion = crear_conexion()
    if conexion is None:
        return False
    else:
        try:
            cursor = conexion.cursor(dictionary=True)
            query = "SELECT * FROM usuario WHERE usuario = %s AND passwd = %s"
            valores = (user, passwd)
            cursor.execute(query, valores)
            resultado = cursor.fetchone()

            if resultado:
                return True # Usuario y contrasena validos
            else:
                return False
        except Exception as e:
            fecha_hora=datetime.datetime.now().strftime("[%d/%m/%Y - %H:%M:%S]")
            file = open("error-db.txt", "a") 
            file.writelines(f"{fecha_hora} | Error: {e} \n")
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()