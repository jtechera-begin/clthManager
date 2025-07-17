import flet as ft
from app.gui.colors import Colores

def cambiar_estado(e):
    checkbox = e.control
    if isinstance(checkbox.label, ft.Text):
        if e.data == "true":
            checkbox.label.color = ft.Colors.GREY
            checkbox.label.decoration = ft.TextDecoration.LINE_THROUGH
        else:
            checkbox.label.color = ft.Colors.WHITE
            checkbox.label.decoration = ft.TextDecoration.NONE
        checkbox.label.update()

class GestorTareas:
    def __init__(self):
        self.tareas = []
        self.lista_tareas = ft.Column(spacing=0)
        self.entrada_tarea = ft.TextField(
            expand=True,
            hint_text="Escribe 4 tareas para hoy",
            hint_style=ft.TextStyle(color=ft.Colors.GREY),
            border_radius=20,
            color=ft.Colors.WHITE,
            border=ft.InputBorder.UNDERLINE,
            border_color= Colores.GRIS_CLARO.value,
            focused_border_color= Colores.AZUL_PRINCIPAL.value
        )

    def agregar_tarea(self, e):
        if len(self.tareas) >= 4:
            print("Máximo de tareas alcanzado")
            return

        texto = self.entrada_tarea.value.strip()
        if texto:
            texto_label = ft.Text(
                texto,
                size=18,
                weight=ft.FontWeight.W_400,
                color=ft.Colors.WHITE 
            )

            checkbox = ft.Checkbox(
                label=texto_label,
                value=False,
                check_color=ft.Colors.WHITE,
                label_position=ft.LabelPosition.RIGHT,
                on_change=cambiar_estado,
            )

            fila_tarea = ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    checkbox,
                    ft.IconButton(
                        icon=ft.Icons.CLOSE,
                        tooltip="Eliminar tarea",
                        style=ft.ButtonStyle(
                            bgcolor=ft.Colors.TRANSPARENT,
                            shape=ft.CircleBorder(),
                            animation_duration=300,
                        ),
                        icon_size=20,
                        on_click=lambda e, chk=checkbox: self.eliminar_tarea(chk),
                    )
                ]
            )

            self.tareas.append(fila_tarea)
            self.entrada_tarea.value = ""
            self.actualizar_lista()

    def actualizar_lista(self):
        self.lista_tareas.controls.clear()
        self.lista_tareas.controls.extend(self.tareas)
        self.lista_tareas.update()

    def obtener_entrada_y_lista(self):
        return self.entrada_tarea, self.lista_tareas
    
    def eliminar_tarea(self, checkbox):
        self.tareas = [fila for fila in self.tareas if checkbox not in fila.controls]
        self.actualizar_lista()
    