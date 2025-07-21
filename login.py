import flet
from flet import *

import app.gui.login_view as login

ruta = ["/login", "/registro"]

def login_form(page: Page):
    page.title = "Login"
    page.window.width = 450
    page.window.height = 550
    page.window.resizable = False
    page.window.center()
    page.padding = 0
    page.theme_mode = ThemeMode.DARK
    page.window.title_bar_hidden = True

    # Función para navegar a otra ruta
    def ir_a_ruta(nueva_ruta: str):
        if nueva_ruta != page.route:
            page.go(nueva_ruta)

    # Cargar vistas
    login_view = login.mostrar_login(page, ir_a_ruta)  # asumimos que esta función recibe page y un callback

    # Función que retorna la vista según la ruta actual
    def mostrar_vista(ruta: str):
        match ruta:
            case "/login":
                return login_view
            case _:
                return Container(Text("Ruta no encontrada", size=20), expand=True)

    # Manejo de cambio de ruta
    def route_change(e):
        page.clean()
        page.add(
            Container(
                bgcolor=Colors.BLACK,
                expand=True,
                content=mostrar_vista(page.route)
            )
        )

    page.on_route_change = route_change
    page.go("/login")

# Lanzar la app
app(target=login_form)