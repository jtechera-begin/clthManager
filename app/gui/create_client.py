import flet
from flet import *

from app.gui.colors import Colores

from app.data.clients_db import ingresar_datos
from app.gui.clientes_view import actualizar_tabla_slienciosa

import time

nombre_completo = TextField(expand=True,label="Nombre completo (*)", hint_text="ej. Juan Perez", autofocus=True, border_radius=10, label_style=TextStyle(weight=FontWeight.W_500),color=Colors.WHITE, bgcolor=Colores.ASIDECOLOR.value, filled=True, fill_color=Colores.ASIDECOLOR.value, border_color=Colores.GRIS_CLARO.value, border=InputBorder.UNDERLINE, hover_color=Colors.TRANSPARENT,focused_border_color=Colores.AZUL_PRINCIPAL.value,)
correo = TextField(expand=True,label="Correo electronico (*)", hint_text="ej. jperez@gmail.com", autofocus=True, border_radius=10, label_style=TextStyle(weight=FontWeight.W_500),color=Colors.WHITE, bgcolor=Colores.ASIDECOLOR.value, filled=True, fill_color=Colores.ASIDECOLOR.value, border_color=Colores.GRIS_CLARO.value, border=InputBorder.UNDERLINE, hover_color=Colors.TRANSPARENT,focused_border_color=Colores.AZUL_PRINCIPAL.value,)
telefono = TextField(max_length=9,expand=True,label="Telefono (*)",hint_text="ej. 095123321", autofocus=True, border_radius=10, label_style=TextStyle(weight=FontWeight.W_500),color=Colors.WHITE, bgcolor=Colores.ASIDECOLOR.value, filled=True, fill_color=Colores.ASIDECOLOR.value, border_color=Colores.GRIS_CLARO.value, border=InputBorder.UNDERLINE, hover_color=Colors.TRANSPARENT,focused_border_color=Colores.AZUL_PRINCIPAL.value,)
direccion = TextField(expand=True,label="Direccion",hint_text="ej. Av. 18 de Julio 1832", autofocus=True, border_radius=10, label_style=TextStyle(weight=FontWeight.W_500),color=Colors.WHITE, bgcolor=Colores.ASIDECOLOR.value, filled=True, fill_color=Colores.ASIDECOLOR.value, border_color=Colores.GRIS_CLARO.value, border=InputBorder.UNDERLINE, hover_color=Colors.TRANSPARENT,focused_border_color=Colores.AZUL_PRINCIPAL.value,)
observacion = TextField(expand=True,label="Observacion",hint_text="ej. Recibe los pedidos en su trabajo",  autofocus=True, border_radius=10, label_style=TextStyle(weight=FontWeight.W_500),color=Colors.WHITE, bgcolor=Colores.ASIDECOLOR.value, filled=True, fill_color=Colores.ASIDECOLOR.value, border_color=Colores.GRIS_CLARO.value, border=InputBorder.UNDERLINE, hover_color=Colors.TRANSPARENT,focused_border_color=Colores.AZUL_PRINCIPAL.value,)
notificacion = Checkbox("El cliente desea recibir notificaciones?", active_color=Colores.AZUL_PRINCIPAL.value, check_color=Colors.WHITE, label_style=TextStyle(weight=FontWeight.W_500, color=Colors.WHITE))

def volver_atras(page: Page, campos: list):
    for campo in campos:
        if isinstance(campo, Checkbox):
            campo.value = False
        else:
            campo.value = ""
    page.update()
    page.go("/clientes")
    actualizar_tabla_slienciosa(page)

def guardar_info(page : Page, nom : str, cor : str, tel : str, dir : str, obs : str, noti : str):
    if nom.strip() != "" and cor.strip() != "" and tel.strip() != "":
        res = ingresar_datos(nom, cor, tel, dir, obs,noti)
        match res:
            case -1 :
                page.open(SnackBar(
                    Text("Error: Parece que no se puede conectar con la base de datos. \n Intente mas tarde", color=Colors.WHITE, weight=FontWeight.BOLD, size=20),
                    bgcolor=Colors.RED,
                    duration=2000
                ))
            case 0 :
                page.open(SnackBar(
                    Text("El cliente se ingresó correctamente", color=Colors.WHITE, weight=FontWeight.BOLD, size=20),
                    bgcolor=Colors.GREEN,
                    duration=2000
                ))
                time.sleep(2)
                volver_atras(page, [nombre_completo, correo, telefono, direccion, observacion, notificacion])
                actualizar_tabla_slienciosa(page)
            case 1:
                page.open(SnackBar(
                    Text("Error: Código 1. \n Contacte con soporte", color=Colors.WHITE, weight=FontWeight.BOLD, size=20),
                    bgcolor=Colors.RED,
                    duration=2000
                ))
            case 2:
                page.open(SnackBar(
                    Text("Error inesperado, consulte el archivo 'error-db.txt'. \n Intente mas tarde", color=Colors.WHITE, weight=FontWeight.BOLD, size=20),
                    bgcolor=Colors.RED,
                    duration=2000
                ))
    else:
        page.open(SnackBar(
                    Text("Aviso: Debes completar al menos los campos obligatorios (*)", color=Colors.WHITE, weight=FontWeight.BOLD, size=20),
                    bgcolor=Colors.ORANGE_300,
                    duration=2000
                ))


def mostrar_create_cliente(page : Page):
    return Container(
        expand=True,
        bgcolor=Colores.NEGRO.value,
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
                            Text("Agregar nuevo cliente", size=25, color=Colors.WHITE, weight=FontWeight.BOLD),
                            IconButton(
                                Icons.ARROW_BACK_IOS_SHARP,
                                style=ButtonStyle(
                                    overlay_color=Colores.GRIS_CLARO.value,
                                    shape=RoundedRectangleBorder(10),
                                    icon_color=Colors.GREY,
                                    animation_duration=500
                                ),
                                on_click=lambda e: volver_atras(page, [nombre_completo, correo, telefono, direccion, observacion, notificacion])
                            ),
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
                                Text(f"Estas a punto de crear nuevos clientes 🚀", size=26, weight=FontWeight.BOLD, color="white"),
                                Text("Ingresá los datos esenciales de tu cliente. La información será almacenada de forma segura y utilizada para futuras gestiones, ventas y seguimiento comercial.", size=16, color="white70"),
                                ElevatedButton(
                                    "Click aquí para ver listado de errores",
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
                    Column(
                        spacing=30,
                        controls=[
                            Column(
                                spacing=2,
                                controls=[
                                    Container(margin=margin.only(20,0,0,0) ,content=(Text("Información personal", size=18, color=Colors.WHITE, weight=FontWeight.W_600))),
                                    Container(
                                        border=border.all(1, Colores.GRIS_CLARO.value),
                                        border_radius=10,
                                        padding=20,
                                        content=nombre_completo
                                    ),
                                ]
                            ),
                            Column(
                                spacing=2,
                                controls=[
                                    Container(margin=margin.only(20,0,0,0),content=(Text("Contacto", size=18, color=Colors.WHITE, weight=FontWeight.W_600))),
                                    Container(
                                        border=border.all(1, Colores.GRIS_CLARO.value),
                                        border_radius=10,
                                        padding=20,
                                        content=Column(
                                            spacing=15,
                                            controls=[
                                                Row(controls=[correo,telefono]),
                                                notificacion
                                            ]
                                        )
                                    )
                                ]
                            ),
                            Column(
                                spacing=2,
                                controls=[
                                    Container(margin=margin.only(20,0,0,0),content=(Text("Extras", size=18, color=Colors.WHITE, weight=FontWeight.W_600))),
                                    Container(
                                        border=border.all(1, Colores.GRIS_CLARO.value),
                                        border_radius=10,
                                        padding=20,
                                        content=Column(
                                            spacing=15,
                                            controls=[
                                                Column(controls=[direccion,observacion]),
                                            ]
                                        )
                                    )
                                ]
                            ),
                            ElevatedButton(
                                "Ingresar",
                                style=ButtonStyle(
                                    bgcolor=Colores.AZUL_PRINCIPAL.value,
                                    color=Colors.WHITE,
                                    padding=20
                                ),
                                on_click=lambda e: guardar_info(page, nombre_completo.value, correo.value, telefono.value, direccion.value, observacion.value, notificacion.value)
                            )
                        ]
                    )
                ]
            )
        )
    )