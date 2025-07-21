import flet
from flet import *
import subprocess
import sys

from app.gui.colors import Colores
#from app.gui.create_client import mostrar_create_cliente

from app.data.clients_db import cargar_datos

tabla_clientes = Column(expand=True, scroll=ScrollMode.AUTO)
texto_cantidad_clientes = Text("", size=15, color=Colors.WHITE, weight=FontWeight.W_600)

def on_hover_tarjeta(e):
    if e.data == "true":
        e.control.bgcolor = Colores.GRIS_CLARO.value
    else:
        e.control.bgcolor = Colores.ASIDECOLOR.value

    e.control.update()

def acciones():
    return Row(
        spacing=3,
        alignment=MainAxisAlignment.CENTER,
        controls=[
            Container(
                width=28,
                height=28,
                alignment=alignment.center,
                content=IconButton(
                    Icons.EDIT_OUTLINED,
                    style=ButtonStyle(
                        padding=0,
                        icon_size=24,
                        overlay_color=Colors.BLUE_100,
                        shape=RoundedRectangleBorder(10),
                        icon_color=Colors.BLUE_ACCENT,
                        animation_duration=500,
                    ),
                    tooltip="Editar datos"
                )
            ),
            Container(
                width=28,
                height=28,
                alignment=alignment.center,
                content=IconButton(
                    Icons.DELETE_OUTLINE_OUTLINED,
                    style=ButtonStyle(
                        padding=0,
                        icon_size=24,
                        overlay_color=Colors.RED_100,
                        shape=RoundedRectangleBorder(10),
                        icon_color=Colors.RED_ACCENT,
                    ),
                    tooltip="Eliminar registro"
                )
            ),
            Container(
                width=28,
                height=28,
                alignment=alignment.center,
                content=IconButton(
                    Icons.INFO_OUTLINED,
                    style=ButtonStyle(
                        padding=0,
                        icon_size=24,
                        overlay_color=Colors.GREY_100,
                        shape=RoundedRectangleBorder(10),
                        icon_color=Colors.GREY,
                    ),
                    tooltip="Ver más"
                )
            )
        ]
    )

def tarjeta_cliente(cliente: dict):
    return Container(
        padding=padding.symmetric(5,10),
        border=border.all(2, Colores.GRIS_CLARO.value),
        border_radius=5,
        content=Row(
            spacing=0,
            controls=[
                Container(width=40, content=Text(str(cliente['ID']))),
                Container(width=120, content=Text(cliente['nombre'])),
                Container(width=190, content=Text(cliente['correo'])),
                Container(width=90, content=Text(str(cliente['telefono']))),
                Container(width=200, content=Text(cliente['direccion'])),
                Container(
                    width=60,
                    margin=margin.only(0,0,20,0),
                    alignment=alignment.center,
                    bgcolor=Colores.DATO_CORRECTO.value if cliente['debe'] else Colores.DATO_INCORRECTO.value,
                    border_radius=5,
                    content=Text(
                        "Sí" if cliente['debe'] else "No",
                        color=Colores.LETRA_DATO_CORRECTO.value if cliente['debe'] else Colores.LETRA_DATO_INCORRECTO.value,
                        weight=FontWeight.BOLD
                    )
                ),
                Container(
                    expand=True,
                    content=acciones()
                ),
            ]
        ),
        #on_click=lambda e: on_click_tarjeta(e),
        on_hover= lambda e: on_hover_tarjeta(e)
    )

def actualizar_tabla_slienciosa(page: Page):
    clientes_nuevo = cargar_datos()

    if clientes_nuevo is None:
        page.open(SnackBar(
            Text("Error al actualizar la tabla: Intente mas tarde", color=Colors.WHITE, weight=FontWeight.BOLD, size=20),
            bgcolor=Colors.RED,
            duration=2000
        ))
    else:
        texto_cantidad_clientes.value = f"{len(clientes_nuevo)} Clientes encontrados"
        texto_cantidad_clientes.update()

        tabla_clientes.controls.clear()
        tabla_clientes.controls.extend([tarjeta_cliente(c) for c in clientes_nuevo])
        tabla_clientes.update()

def actualizar_tabla(page : Page):
    clientes_nuevo = cargar_datos()

    if clientes_nuevo is None:
        page.open(SnackBar(
            Text("Error al actualizar la tabla: Intente mas tarde", color=Colors.WHITE, weight=FontWeight.BOLD, size=20),
            bgcolor=Colors.RED,
            duration=2000
        ))
    else:
        page.open(SnackBar(
            Text("Tabla actualizada correctamente", color=Colors.WHITE, weight=FontWeight.BOLD, size=20),
            bgcolor=Colors.GREEN,
            duration=2000
        ))
        texto_cantidad_clientes.value = f"{len(clientes_nuevo)} Clientes encontrados"
        texto_cantidad_clientes.update()

        tabla_clientes.controls.clear()
        tabla_clientes.controls.extend([tarjeta_cliente(c) for c in clientes_nuevo])
        tabla_clientes.update()
    

def mostrar_clientes(page : Page):
    clientes = cargar_datos()
    tabla_clientes.controls.clear()
    filas_clientes = [tarjeta_cliente(c) for c in clientes]

    texto_cantidad_clientes.value = f"{len(clientes)} Clientes encontrados"

    tabla_clientes.controls.extend(filas_clientes)

    return Container(
        expand=True,
        bgcolor=Colores.NEGRO.value,
        height=1000,
        content=Container(
            expand=True,
            bgcolor=Colores.ASIDECOLOR.value,
            padding=30,
            margin=margin.only(30,0,30,30),
            border_radius=30,
            content=Column(
                expand=True,
                spacing=75,
                scroll=ScrollMode.AUTO,
                controls=[
                    Row(
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            Column(
                                controls=[
                                    Text("Clientes", size=25, color=Colors.WHITE, weight=FontWeight.BOLD),
                                    texto_cantidad_clientes
                                ]
                            ),
                            ElevatedButton(
                                "Agregar nuevo cliente",
                                icon=Icons.ADD,
                                style=ButtonStyle(
                                    bgcolor=Colores.AZUL_PRINCIPAL.value,
                                    color=Colors.WHITE,
                                    padding=20
                                ),
                                on_click=lambda e: page.go("/alta_cliente")
                            )
                        ]
                    ),
                    Column(
                        spacing=15,
                        controls=[
                            Row(
                                expand=True,
                                alignment=MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    Row(
                                        spacing=30,
                                        controls=[
                                            Text("Clientes activos", size=18, weight=FontWeight.W_600, color=Colors.WHITE),
                                            TextField(
                                                width=400,
                                                hint_text="Busca un cliente por id, nombre, telefono...",
                                                hint_style=TextStyle(
                                                    color=Colors.GREY
                                                ),
                                                border_radius=20,
                                                prefix_icon=Icons.SEARCH,
                                                height=45,
                                                filled=True,
                                                color=Colors.WHITE,
                                                fill_color=Colores.ASIDECOLOR.value,
                                                border_color=Colores.GRIS_CLARO.value,
                                                border=InputBorder.UNDERLINE,
                                                focused_border_color=Colores.AZUL_PRINCIPAL.value,
                                                hover_color=Colors.TRANSPARENT,
                                            )
                                        ]
                                    ),
                                    Row(
                                        spacing=3,
                                        controls=[
                                            IconButton(
                                                Icons.UPDATE,
                                                tooltip="Actualizar tabla",
                                                style=ButtonStyle(
                                                    overlay_color=Colores.GRIS_CLARO.value,
                                                    shape=RoundedRectangleBorder(10),
                                                    icon_color=Colors.GREY,
                                                    animation_duration=500
                                                ),
                                                on_click=lambda e: actualizar_tabla(page)
                                            ),
                                            ElevatedButton(
                                                "Ver inactivos",
                                                icon=Icons.ARROW_DROP_DOWN_ROUNDED,
                                                tooltip="Ver clientes inactivos",
                                                style=ButtonStyle(
                                                    bgcolor=Colores.ASIDECOLOR.value,
                                                    icon_color=Colors.GREY,
                                                    color=Colors.GREY,
                                                    overlay_color=Colores.GRIS_CLARO.value,
                                                    shape=RoundedRectangleBorder(10),
                                                    animation_duration=500
                                                ),
                                            ),
                                            ElevatedButton(
                                                "Exportar",
                                                icon=Icons.UPLOAD_FILE,
                                                tooltip="Exportar tabla como EXCEL",
                                                style=ButtonStyle(
                                                    bgcolor=Colores.ASIDECOLOR.value,
                                                    icon_color=Colors.GREY,
                                                    color=Colors.GREY,
                                                    overlay_color=Colores.GRIS_CLARO.value,
                                                    shape=RoundedRectangleBorder(10),
                                                    animation_duration=500
                                                ),
                                            )
                                        ]
                                    )
                                ]
                            ),
                            Container(
                                bgcolor=Colores.GRIS_CLARO.value,
                                padding=10,
                                border_radius=5,
                                content=Row(
                                    spacing=0,
                                    controls=[
                                        Container(width=40, content=Text("ID", weight=FontWeight.BOLD)),
                                        Container(width=120, content=Text("Nombre", weight=FontWeight.BOLD)),
                                        Container(width=190, content=Text("Correo", weight=FontWeight.BOLD)),
                                        Container(width=90, content=Text("Teléfono", weight=FontWeight.BOLD)),
                                        Container(width=200, content=Text("Dirección", weight=FontWeight.BOLD)),
                                        Container(alignment=alignment.center,width=60, margin=margin.only(0,0,45,0),content=Text("Debe", weight=FontWeight.BOLD)),
                                        Container(alignment=alignment.center, width=80, content=Text("Acción", weight=FontWeight.BOLD))
                                    ]
                                )
                            ),
                            tabla_clientes
                        ]
                    )
                ]
            )
        )
    )