import json
import os
from app.logic.user import User

RUTA_ARCHIVO_SESION = "sesion.json"

def guardar_sesion_json(usuario: User):
    with open(RUTA_ARCHIVO_SESION, "w") as f:
        json.dump({
            "nombre": usuario.nombre,
            "correo": usuario.correo,
            "rol": usuario.rol
        }, f)

def cargar_sesion_json():
    if not os.path.exists(RUTA_ARCHIVO_SESION):
        return None

    try:
        with open(RUTA_ARCHIVO_SESION, "r") as f:
            datos = json.load(f)
            return User(datos["nombre"], datos["correo"], datos["rol"])
    except (json.JSONDecodeError, KeyError):
        return None

def cerrar_sesion_json():
    if os.path.exists(RUTA_ARCHIVO_SESION):
        os.remove(RUTA_ARCHIVO_SESION)