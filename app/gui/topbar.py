import flet
from flet import *
from app.gui.colors import Colores

def cerrar(page : Page):
    page.window.close() 

def minimizar(page : Page):
    page.window.minimized = True
    page.update()

def mostrar_topbar(page : Page):
    return Container(
        bgcolor=Colores.NEGRO.value,
        padding=padding.symmetric(10,30),
        content=Row(
            alignment=MainAxisAlignment.END,
            controls=[
                Row(
                    controls=[
                        IconButton(
                            Icons.MINIMIZE,
                            icon_color=Colores.BLANCO.value,
                            on_click=lambda e: minimizar(page)
                        ),
                        IconButton(
                            Icons.CLOSE,
                            icon_color=Colores.BLANCO.value,
                            on_click=lambda e: cerrar(page)
                        )
                    ]
                )
            ]
        )
    )