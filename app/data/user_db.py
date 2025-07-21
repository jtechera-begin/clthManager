from app.logic.user import User
from app.data.db_connection import crear_conexion

def obtener_datos_usuario(nombre_usuario):
    conexion = crear_conexion()
    cursor = conexion.cursor()
    query = "SELECT usuario, correo, rol FROM usuario WHERE usuario = %s"
    cursor.execute(query, (nombre_usuario,))
    resultado = cursor.fetchone()
    conexion.close()

    if resultado:
        return User(*resultado)
    else:
        return None
