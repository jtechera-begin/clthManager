import flet
from flet import *

import subprocess
import sys
from app.gui.colors import Colores

from app.data.login_function import iniciar_sesion
from app.data.user_db import obtener_datos_usuario
from app.logic.session_storage import guardar_sesion_json

usuario = TextField(label="Nombre de usuario", autofocus=True, border_radius=10, label_style=TextStyle(weight=FontWeight.W_500),color=Colors.WHITE, bgcolor=Colores.ASIDECOLOR.value)
contrasena = TextField(label="Contraseña", password=True, can_reveal_password=True, border_radius=10, label_style=TextStyle(weight=FontWeight.W_500),color=Colors.WHITE, bgcolor=Colores.ASIDECOLOR.value)

def ingresar(nombre, passwd, page : Page):
    if iniciar_sesion(nombre, passwd):
        usr = obtener_datos_usuario(nombre)
        if usr:
            guardar_sesion_json(usr)

        page.window.close()
        subprocess.Popen([sys.executable, "main.py"])
    else:
        page.open(SnackBar(
            Text("Usuario y/o contraseña equivocado.", color=Colors.WHITE),
            bgcolor=Colors.RED,
            duration=2000
            ))
        page.update()

def cerrar(page : Page):
    page.window.close() 

def cambiar_link(e):
    if e.data == "true":
        e.control.style = ButtonStyle(
                                text_style=TextStyle(decoration=TextDecoration.UNDERLINE),
                                color=Colores.AZUL_PRINCIPAL.value,
                                mouse_cursor=MouseCursor.CLICK,
                                overlay_color=Colors.TRANSPARENT)
    else:
        e.control.style = ButtonStyle(
                                text_style=TextStyle(decoration=TextDecoration.NONE),
                                color=Colores.AZUL_PRINCIPAL.value,
                                mouse_cursor=MouseCursor.CLICK,
                                overlay_color=Colors.TRANSPARENT)
    e.control.update()

def mostrar_login(page, ir_a_ruta):
    return Container(
        expand=True,
        padding=padding.only(0,50,0,0),
        alignment=alignment.center,
        bgcolor=Colores.NEGRO.value,
        content=Column(
            controls=[
                Container(
                    padding=padding.only(40,30,40,20),
                    content=Row(
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            Text("Iniciar Sesion", size=30, weight=FontWeight.W_300, color=Colores.BLANCO.value),
                            IconButton(
                                Icons.CLOSE,
                                icon_color=Colores.BLANCO.value,
                                on_click=lambda e: cerrar(page)
                            )
                        ]
                    )
                ),

                Container(
                    padding=padding.only(40,30,40,0),
                    content=Column(
                        expand=True,
                        controls=[
                            usuario,
                            contrasena,
                        ]
                    )
                ),
                Container(
                    padding=padding.only(40,0,0,0),
                    content=Row(
                        alignment=MainAxisAlignment.START,
                        spacing=1,
                        controls=[
                            Text("¿Olvidaste tu contraseña?"),
                            TextButton(
                                "Recuperar",
                                style=ButtonStyle(
                                    text_style=TextStyle(decoration=TextDecoration.NONE),
                                    color=Colores.AZUL_PRINCIPAL.value,
                                    mouse_cursor=MouseCursor.CLICK,
                                    animation_duration=0,
                                    overlay_color=Colors.TRANSPARENT,
                                ),
                                on_hover=lambda e: cambiar_link(e)
                                #on_click=lambda e: recuperar_passwd
                                #recuperar_passwd: posible pregunta que solo el usuario sepa responder para dar acceso
                            )
                        ]
                    ),
                ),
                Container(
                    padding=padding.only(40,20,40,0),
                    content=Row(
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            ElevatedButton(
                                "Ingresar",
                                expand=True,
                                style=ButtonStyle(
                                    bgcolor=Colores.AZUL_PRINCIPAL.value,
                                    color=Colors.WHITE,
                                    shape=RoundedRectangleBorder(radius=10),
                                    padding=20
                                ),
                                on_click=lambda e: ingresar(usuario.value, contrasena.value, page)
                            )
                        ]
                    )
                ),
            ]
        )
    )