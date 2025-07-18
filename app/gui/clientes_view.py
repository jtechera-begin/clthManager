import flet
from flet import *

from app.gui.colors import Colores

def mostrar_clientes():
    return Container(
        expand=True,
        bgcolor=Colores.NEGRO.value,
        content=Container(
            expand=True,
            bgcolor=Colores.ASIDECOLOR.value,
            padding=30,
            margin=30,
            border_radius=30,
        )
    )