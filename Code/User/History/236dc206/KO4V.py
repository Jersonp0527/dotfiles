import flet as ft

def main(page: ft.Page):
    # Creamos los paneles (vistas) que se mostrarán para cada sección
    saved_panel = ft.Text("Guardados")
    explore_panel = ft.Text("Explorar")
    settings_panel = ft.Text("Configuraciones")

    # Contenedor para el contenido que cambiará
    # Por defecto, mostramos la vista "Explorar"
    content = ft.Column([explore_panel])

    # Función para manejar el cambio de pestaña
    def on_nav_change(e):
        # Cambiamos el contenido del panel según la pestaña seleccionada
        if page.navigation_bar.selected_index == 0:
            content.controls = [saved_panel]
        elif page.navigation_bar.selected_index == 1:
            content.controls = [explore_panel]
        elif page.navigation_bar.selected_index == 2:
            content.controls = [settings_panel]

        # Actualizamos la página para reflejar los cambios
        page.update()

    # Configuramos el título de la página
    page.title = "HealthMate"

    # Creamos la barra de navegación
    # Iniciamos con la pestaña "Explorar" seleccionada (índice 1)
    page.navigation_bar = ft.NavigationBar(
        selected_index=1,  # Por defecto, seleccionamos la pestaña "Explorar"
        on_change=on_nav_change,  # Llamamos a la función cuando cambia la pestaña
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.BOOKMARK, label="Guardados"),
            ft.NavigationBarDestination(icon=ft.icons.EXPLORE, label="Explorar"),
            ft.NavigationBarDestination(icon=ft.icons.SETTINGS, label="Configuraciones"),
        ]
    )

    # Añadimos el contenedor del contenido dinámico a la página
    page.add(content)

# Iniciamos la aplicación llamando a la función principal
ft.app(main)
