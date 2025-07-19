import flet
from flet import *
import subprocess
import sys
from app.gui.colors import Colores

usuario = TextField(label="Nombre de usuario", autofocus=True, border_radius=10, label_style=TextStyle(weight=FontWeight.W_500),color=Colors.WHITE, bgcolor=Colores.ASIDECOLOR.value)
contrasena = TextField(label="Contraseña", password=True, can_reveal_password=True, border_radius=10, label_style=TextStyle(weight=FontWeight.W_500),color=Colors.WHITE, bgcolor=Colores.ASIDECOLOR.value)
mensaje = Row(alignment=MainAxisAlignment.CENTER,controls=[Text("Credenciales invalidas", color=Colors.RED)])
mensaje.opacity = 0

def ingresar(nombre, passwd, page : Page):
    if nombre == "Juan" and passwd == "1234":
        page.window.close()
        subprocess.Popen([sys.executable, "main.py"])
    else:
        mensaje.opacity = 1
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

def login(page, mensaje):
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
                            )
                        ]
                    ),
                ),
                mensaje,
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
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    spacing=1,
                    controls=[
                        Text("¿Todavia no tenes una cuenta?"),
                        TextButton(
                            "Registrate!",
                            style=ButtonStyle(
                                text_style=TextStyle(decoration=TextDecoration.NONE),
                                color=Colores.AZUL_PRINCIPAL.value,
                                mouse_cursor=MouseCursor.CLICK,
                                animation_duration=0,
                                overlay_color=Colors.TRANSPARENT,
                            ),
                            on_hover=lambda e: cambiar_link(e)
                        )
                    ]
                ),
            ]
        )
    )

def login_form(page : Page):
    page.title = "Login"
    page.window.width = 450
    page.window.height = 550
    page.window.resizable = False
    page.window.center()
    page.padding = 0
    page.theme_mode = ThemeMode.DARK
    page.window.title_bar_hidden = True

    page.add(
        login(page, mensaje)
    )

app(target=login_form)