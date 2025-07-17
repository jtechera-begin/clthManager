import flet
from flet import *

from app.gui.colors import Colores

def mostrar_clientes():
    return Container(
        bgcolor=Colores.ASIDECOLOR.value,
        expand=True
    )