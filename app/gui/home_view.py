import flet
from flet import *

from app.gui.colors import Colores
from app.logic.todo import GestorTareas

gestor = GestorTareas()
entrada, lista = gestor.obtener_entrada_y_lista()

def crear_cartas(text, number):
    return Container(
        width=180,
        height=100,
        border_radius=10,
        padding=20,
        bgcolor=Colores.GRIS_CLARO.value,
        content=Column(
            controls=[
                Text(text, size=16, color=Colors.WHITE, weight=FontWeight.W_700),
                Text(number, size=22, color=Colores.AZUL_PRINCIPAL.value, weight=FontWeight.BOLD)
            ]
        )
    )

def on_hover(e):
    if e.data == "true":
        e.control.style = ButtonStyle(
            bgcolor=Colores.AZUL_PRINCIPAL.value,
            icon_color=Colores.BLANCO.value,
            shape=RoundedRectangleBorder(radius=10)
        )
    else:
        e.control.style = ButtonStyle(
            bgcolor=Colors.TRANSPARENT,
            shape=CircleBorder()
        )
    e.control.update()

def mostrar_home():
    return Container(
        expand=True,
        bgcolor=Colores.NEGRO.value,
        content=Container(
            expand=True,
            bgcolor=Colores.ASIDECOLOR.value,
            padding=30,
            margin=30,
            border_radius=30,
            content=Column(
                spacing=20,
                controls=[
                    Row(
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            TextField(
                                hint_text="Search something...",
                                hint_style=TextStyle(
                                    color=Colors.GREY
                                ),
                                border_radius=20,
                                prefix_icon=Icons.SEARCH,
                                width=600,
                                height=45,
                                filled=True,
                                color=Colors.WHITE,
                                fill_color=Colores.ASIDECOLOR.value,
                                border_color=Colors.TRANSPARENT,
                                focused_border_color=Colores.AZUL_PRINCIPAL.value,
                                hover_color=Colors.TRANSPARENT,
                            ),
                            ElevatedButton(
                                "Add New",
                                icon=Icons.ADD,
                                style=ButtonStyle(
                                    bgcolor=Colores.AZUL_PRINCIPAL.value,
                                    color=Colors.WHITE,
                                    shape=RoundedRectangleBorder(radius=20),
                                    padding=20
                                )
                            )
                        ]
                    ),

                    Container(
                        padding=30,
                        bgcolor=Colores.AZUL_PRINCIPAL.value,
                        border_radius=20,
                        alignment=alignment.center_left,
                        content=Column(
                            alignment=MainAxisAlignment.CENTER,
                            spacing=10,
                            horizontal_alignment=CrossAxisAlignment.START,
                            controls=[
                                Text("Good Morning", size=26, weight=FontWeight.BOLD, color="white"),
                                Text("You have 75 new applications. It is a lot of work for today!", size=16, color="white70"),
                                ElevatedButton(
                                    "Review It",
                                    icon=Icons.CHECK_CIRCLE_OUTLINE,
                                    style=ButtonStyle(
                                        bgcolor="white",
                                        color=Colors.BLUE_800,
                                        shape=RoundedRectangleBorder(radius=20),
                                        padding=10
                                    )
                                )
                            ]
                        )
                    ),

                    Container(
                        expand=True,
                        content=Container(
                            expand=True,
                            content=Row(
                                alignment=MainAxisAlignment.SPACE_BETWEEN,
                                spacing=10,
                                expand=True,
                                controls=[
                                    Container(
                                        bgcolor=Colores.ASIDECOLOR.value,
                                        width=425,
                                        border_radius=20,
                                        padding=30,
                                        content=Column(
                                            expand=True,
                                            horizontal_alignment=MainAxisAlignment.START,
                                            spacing=10,
                                            controls=[
                                                Text("Informes actuales", size=20, weight=FontWeight.BOLD, color=Colores.TEXTO.value),
                                                Column(
                                                    expand=True,
                                                    spacing=10,
                                                    alignment=MainAxisAlignment.START,
                                                    controls=[
                                                        Row(
                                                            spacing=10,
                                                            alignment=MainAxisAlignment.SPACE_BETWEEN,
                                                            controls=[
                                                                crear_cartas("V. de la semana", "$200"),
                                                                crear_cartas("Clientes actuales", "30"),
                                                            ]
                                                        ),
                                                        Row(
                                                            alignment=MainAxisAlignment.SPACE_BETWEEN,
                                                            spacing=10,
                                                            controls=[
                                                                crear_cartas("Ventas del mes", "$1200"),
                                                                crear_cartas("Beneficio Neto", "$700"),
                                                            ]
                                                        )
                                                    ]
                                                )
                                            ]
                                        ),
                                    ),
                                    Container(
                                        bgcolor=Colores.ASIDECOLOR.value,
                                        width=450,
                                        border_radius=20,
                                        padding=30,
                                        content=Column(
                                            expand=True,
                                            controls=[
                                                Row(
                                                    controls=[
                                                        Text("Tareas para hoy", size=20, weight=FontWeight.BOLD, color=Colores.TEXTO.value),
                                                    ]
                                                ),
                                                Row(
                                                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                                                    controls=[
                                                        entrada,
                                                        IconButton(
                                                            icon=Icons.ADD,
                                                            icon_size=20,
                                                            tooltip="Agregar",
                                                            on_hover=lambda e: on_hover(e),
                                                            style=ButtonStyle(
                                                                bgcolor=Colors.TRANSPARENT,
                                                                padding=10,
                                                                shape=CircleBorder(),
                                                                animation_duration=300
                                                            ),
                                                            on_click= lambda e: gestor.agregar_tarea(e),
                                                        )
                                                    ]
                                                ),
                                                lista
                                            ]
                                        ),
                                    ),
                                ]
                            )
                        )
                    )
                ]
            )
        )
    )
