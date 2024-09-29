import flet as ft

def main(page: ft.Page):

    # Creamos los paneles (vistas) que se mostrarán para cada sección
    saved_panel = ft.Text("Guardados")
    explore_panel = ft.Text("Explorar")
    settings_panel = ft.Text("Configuraciones")

    # Contenedor para el contenido que cambiará
    content = ft.Column([explore_panel])  # Por defecto, mostramos la vista "Explorar"

    # Función para manejar el cambio de pestaña
    def on_nav_change(e):
        if page.navigation_bar.selected_index == 0:
            content.controls = [saved_panel]
        elif page.navigation_bar.selected_index == 1:
            content.controls = [explore_panel]
        elif page.navigation_bar.selected_index == 2:
            content.controls = [settings_panel]
        page.update()

    # Configuramos el título de la página
    page.title = "NavigationBar Example"
    
    # Creamos la barra de navegación
    page.navigation_bar = ft.NavigationBar(
        selected_index=1,  # Comenzamos con la pestaña de "Explorar"
        on_change=on_nav_change,
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.BOOKMARK, label="Guardados"),
            ft.NavigationBarDestination(icon=ft.icons.EXPLORE, label="Explorar"),
            ft.NavigationBarDestination(icon=ft.icons.SETTINGS, label="Configuraciones"),
        ]
    )
    
    # Añadimos el contenedor del contenido dinámico a la página
    page.add(content)

ft.app(main)
