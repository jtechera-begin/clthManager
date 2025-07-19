import flet
from flet import *
from app.gui.colors import Colores
import subprocess
import sys

def on_hover(e):
    if e.data == "true":
        e.control.bgcolor = Colores.GRIS_CLARO.value
        #e.control.content.controls[0].icon_color = Colores.AZUL_PRINCIPAL.value
        #e.control.content.controls[1].color = Colores.AZUL_PRINCIPAL.value
    else:
        e.control.bgcolor = Colores.ASIDECOLOR.value
        #e.control.content.controls[0].icon_color = Colores.FONDO.value
        #e.control.content.controls[1].color = Colores.FONDO.value
    e.control.update()

def volver_a_login(page : Page):
    page.window.close()
    subprocess.Popen([sys.executable, "login.py"])

def boton_salir(icon_name: str, text: str, page : Page):
    return GestureDetector(
        mouse_cursor=MouseCursor.CLICK,
        on_tap=lambda e: volver_a_login(page),
        content=Container(
            width=200,
            height=45,
            border_radius=10,
            bgcolor=Colores.ASIDECOLOR.value,
            on_hover=on_hover,
            content=Row(
                controls=[
                    IconButton(
                        icon=icon_name,
                        icon_color=Colores.TEXTO.value,
                        icon_size=18,
                        style=ButtonStyle(
                            shape=RoundedRectangleBorder(radius=5),
                            overlay_color="Transparent"
                        ),
                    ),
                    Text(
                        value=text,
                        color=Colores.TEXTO.value,
                        size=13
                    )
                ]
            ),
            opacity=0.9
        )
    )

def botones(icon_name: str, text: str, ruta: str, ir_a_ruta):
    return GestureDetector(
        mouse_cursor=MouseCursor.CLICK,
        on_tap=lambda e: ir_a_ruta(ruta),
        content=Container(
            width=200,
            height=45,
            border_radius=10,
            bgcolor=Colores.ASIDECOLOR.value,
            on_hover=on_hover,
            content=Row(
                controls=[
                    IconButton(
                        icon=icon_name,
                        icon_color=Colores.TEXTO.value,
                        icon_size=18,
                        style=ButtonStyle(
                            shape=RoundedRectangleBorder(radius=5),
                            overlay_color="Transparent"
                        ),
                    ),
                    Text(
                        value=text,
                        color=Colores.TEXTO.value,
                        size=13
                    )
                ]
            ),
            opacity=0.9
        )
    )

def perfil():
    return Container(
        width=100,
        height=100,
        border_radius=100,
        bgcolor=Colores.BLANCO.value,
        margin=margin.symmetric(0,50)
    )

def mostrar_nav(ir_a_ruta, page : Page):
    return Container(
        bgcolor=Colores.NEGRO.value,
        content=Container(
            width=230,
            height=720,
            padding=padding.symmetric(60, 0),
            margin=margin.only(30, 0, 0, 30),
            border_radius=30,
            bgcolor=Colores.ASIDECOLOR.value,
            alignment=alignment.center,
            content=Column(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    Column(
                        alignment=CrossAxisAlignment.CENTER,
                        controls=[perfil()]
                    ),
                    Column(
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                        controls=[
                            botones(Icons.HOME, "Inicio", "/home", ir_a_ruta),
                            botones(Icons.PERSON, "Clientes", "/clientes", ir_a_ruta),
                            botones(Icons.SHOPPING_BAG, "Ventas", "/ventas", ir_a_ruta),
                        ],
                    ),
                    boton_salir(Icons.EXIT_TO_APP, "Volver a Login", page)
                ]
            )
        )
    )