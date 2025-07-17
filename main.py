import flet
from flet import *
from app.gui.colors import Colores

import app.gui.navbar as nav
import app.gui.home_view as home
import app.gui.clientes_view as clients
import app.gui.ventas_view as ventas

ruta = ["/", "/clientes", "/ventas", "/salir"]

def main(page: Page):
    page.title = "Sistema de gestión"
    page.window.width = 1280
    page.window.height = 720
    page.window.max_width = 1280
    page.window.max_height = 720
    page.window.maximizable = False
    page.window.center()
    page.window.resizable = False
    page.padding = 0
    page.update()

    def ir_a_ruta(nueva_ruta: str):
        if nueva_ruta != page.route:
            page.go(nueva_ruta)

    navbar = nav.mostrar_nav(ir_a_ruta)

    home_view=home.mostrar_home()
    clients_view=clients.mostrar_clientes()
    ventas_view=ventas.mostrar_ventas()

    def mostrar_vista(ruta:str):
        vista = Container(expand=True)
        match ruta:
            case "/" | "/home":
                return home_view
            case "/clientes":
                return clients_view
            case "/ventas":
                return ventas_view
            case "/salir":
                page.window.destroy()
                return
            case _:
                return Container(Text("Ruta no encontrada", size=20), expand=True)

    def route_change(e):
        page.clean()
        page.add(
            Container(
                bgcolor=Colors.WHITE,
                expand=True,
                content=Row(
                    expand=True,
                    spacing=0,
                    controls=[navbar, mostrar_vista(page.route)]
                )
            )
        )

    page.on_route_change = route_change
    page.go("/")
app(target=main)